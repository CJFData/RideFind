import streamlit as st
import geopandas as gpd
import pandas as pd
import folium
from shapely.geometry import LineString
from shapely.ops import unary_union
import zipfile
import requests
from streamlit_folium import st_folium

st.set_page_config(page_title="RideFind - Transit Buffer Tool", layout="wide")
st.title("🚍 RideFind: Transit Network & ¾-Mile Buffer Tool")

# -------------------------------
# GTFS UPLOAD
# -------------------------------
gtfs_file = st.file_uploader("Upload GTFS ZIP File", type=["zip"])

if gtfs_file is not None:
    with zipfile.ZipFile(gtfs_file, "r") as z:
        if "shapes.txt" not in z.namelist():
            st.error("GTFS file must include shapes.txt")
            st.stop()
        shapes_df = pd.read_csv(z.open("shapes.txt"))

    shapes_df.sort_values(by=["shape_id", "shape_pt_sequence"], inplace=True)

    # Build route lines
    shape_lines = (
        shapes_df.groupby("shape_id")
        .apply(lambda x: LineString(zip(x["shape_pt_lon"], x["shape_pt_lat"])))
    )

    gdf_shapes = gpd.GeoDataFrame(
        {"shape_id": shape_lines.index, "geometry": shape_lines.values},
        crs="EPSG:4326"
    )

    # ¾-mile buffer (~1207 meters)
    gdf_proj = gdf_shapes.to_crs(3857)
    gdf_buffer = gdf_proj.buffer(1207.01)
    gdf_buffer = gpd.GeoDataFrame(geometry=gdf_buffer, crs=3857).to_crs(4326)
    buffer_union = unary_union(gdf_buffer.geometry)

    st.success("GTFS loaded successfully!")

    # -------------------------------
    # Initialize session_state
    # -------------------------------
    if "show_map" not in st.session_state:
        st.session_state.show_map = False

    for prefix in ["start", "end"]:
        if f"{prefix}_address" not in st.session_state:
            st.session_state[f"{prefix}_address"] = None
            st.session_state[f"{prefix}_lat"] = None
            st.session_state[f"{prefix}_lon"] = None

    # -------------------------------
    # ADDRESS SEARCH INPUTS
    # -------------------------------
    st.write("### 🔎 Address Search")
    start_query = st.text_input("Start Address:")
    end_query = st.text_input("End Address:")

    # Function to search addresses via Nominatim
    def search_address(query):
        if query and len(query) > 3:
            url = "https://nominatim.openstreetmap.org/search"
            params = {"q": query, "format": "json", "addressdetails": 1, "limit": 7}
            resp = requests.get(url, params=params, headers={"User-Agent": "streamlit-ridefind-app"})
            if resp.ok:
                results = resp.json()
                if results:
                    suggestions = [r["display_name"] for r in results]
                    return suggestions, results
        return [], []

    # Search results
    start_suggestions, start_results = search_address(start_query)
    end_suggestions, end_results = search_address(end_query)

    # Select boxes
    selected_start = st.selectbox("Select Start Address:", start_suggestions) if start_suggestions else None
    selected_end = st.selectbox("Select End Address:", end_suggestions) if end_suggestions else None

    # -------------------------------
    # SHOW MAP BUTTON
    # -------------------------------
    if st.button("Show on Map"):
        # Save selections to session state
        for name, results, selected in [("start", start_results, selected_start), ("end", end_results, selected_end)]:
            if selected:
                for r in results:
                    if r["display_name"] == selected:
                        st.session_state[f"{name}_address"] = selected
                        st.session_state[f"{name}_lat"] = float(r["lat"])
                        st.session_state[f"{name}_lon"] = float(r["lon"])
                        break
        st.session_state.show_map = True

    # -------------------------------
    # BUILD MAP
    # -------------------------------
    if st.session_state.show_map:
        m = folium.Map(
            location=[shapes_df.shape_pt_lat.mean(), shapes_df.shape_pt_lon.mean()],
            zoom_start=12
        )

        # Add transit lines
        for _, row in gdf_shapes.iterrows():
            folium.GeoJson(
                row.geometry,
                style_function=lambda x: {"color": "blue", "weight": 2}
            ).add_to(m)

        # Add buffer
        folium.GeoJson(
            buffer_union,
            style_function=lambda x: {"color": "green", "fillOpacity": 0.25}
        ).add_to(m)

        # Add markers for start and end addresses
        for prefix in ["start", "end"]:
            if st.session_state[f"{prefix}_address"]:
                pt = gpd.GeoDataFrame(
                    geometry=[gpd.points_from_xy([st.session_state[f"{prefix}_lon"]], [st.session_state[f"{prefix}_lat"]])[0]],
                    crs="EPSG:4326"
                )
                inside_buffer = pt.within(buffer_union)[0]
                marker_color = "green" if inside_buffer else "red"
                if inside_buffer:
                    st.success(f"🏆 {prefix.capitalize()} address is within ¾ mile of the transit network.")
                else:
                    st.error(f"❌ {prefix.capitalize()} address is outside the ¾-mile buffer.")

                folium.Marker(
                    [st.session_state[f"{prefix}_lat"], st.session_state[f"{prefix}_lon"]],
                    popup=st.session_state[f"{prefix}_address"],
                    icon=folium.Icon(color=marker_color)
                ).add_to(m)

        st.write("### 🗺️ Transit Network Map")
        st_folium(m, width=800, height=550)

        # Download HTML
        html_string = m.get_root().render()
        st.download_button(
            label="⬇ Download HTML Map",
            data=html_string,
            file_name="transit_buffer_map.html",
            mime="text/html"
        )

