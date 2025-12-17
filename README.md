# 🚍 RideFind - Transit Network Proximity Checker

A Streamlit web application that helps transit professionals determine if an address is within 3/4 mile of their transit service network using GTFS data.

## ⚠️ Important Disclaimer

**THIS CODE DOES NOT REPLACE PROFESSIONAL ANALYSIS OR FTA/OTHER GRANTOR COMPLIANCE REQUIREMENTS.** It does not account for every transit authority's specific situation regarding service modes and ADA compliance requirements. Use of this app is at your own discretion. All reporting and compliance with FTA policy and other grantors should be done with close reference to each grantor's policy manuals to ensure full compliance.

## 🚀 Live Demo

**Web App**: https://ridefind.streamlit.app/

## ✨ Features

- **GTFS File Upload**: Upload your transit agency's GTFS feed
- **Address Search**: Search any address with autocomplete functionality
- **Interactive Map**: View your transit network plotted on an interactive Folium map
- **3/4 Mile Buffer Visualization**: See the ADA-compliant service area buffer around transit routes
- **Address Location**: Pinpoint searched addresses on the map with a green marker
- **Downloadable Maps**: Export maps as HTML files for documentation and reporting
- **All Service Modes**: Plots all shapes from GTFS regardless of service mode

## 📋 Use Case

Whether a trip starts or ends within the 3/4 mile zone buffer is used for ADA program requirements. RideFind helps transit professionals quickly verify if an address falls within this service area. *Note: Use of this app does not guarantee full compliance with ADA guidelines.*

## 🛠️ Installation

### Option 1: Use the Web App
Simply visit https://ridefind.streamlit.app/ - no installation needed!

### Option 2: Local Installation

1. Clone this repository:
```bash
git clone https://github.com/CJFData/RideFind.git
cd RideFind
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run RideFind.py
```

4. Open your browser to `http://localhost:8501`

### Option 3: Jupyter Notebook

You can run this as Jupyter notebook cells:

**Cell 1** - Install libraries:
```python
!python LibraryInstall.py
```

**Cell 2** - Run the app:
```python
!streamlit run RideFind.py --server.headless true
```

## 📖 How to Use

### Step 1: Upload GTFS File
Click the upload button and select your transit agency's GTFS .zip file.

![Upload GTFS](https://private-user-images.githubusercontent.com/248803650/524628706-93b157fb-611d-49e6-a3f7-c723d1ee2cd6.png)

### Step 2: Search Address
Enter the address you want to check. The app provides autocomplete suggestions - be sure to include at least the street address and town.

![Search Address](https://private-user-images.githubusercontent.com/248803650/524629102-ce30fb06-f9db-48b4-8e67-a57e04f7b439.png)

### Step 3: View on Map
Click "Show On Map" to plot the transit network from your GTFS file with the 3/4 mile buffer. The searched address appears as a green pin.

![View Map](https://private-user-images.githubusercontent.com/248803650/524629525-6fa522f2-43d4-479f-abe1-755575b88fc9.png)

### Step 4: Download Map (Optional)
Save the map by clicking "Download HTML Map" for your records or reports.

![Download Map](https://private-user-images.githubusercontent.com/248803650/524629769-8f801b28-fc25-4281-a4ff-4c6847313f52.png)

## 📦 Requirements

- Python 3.7+
- streamlit
- folium
- geopandas
- shapely
- pandas
- gtfs-kit (or similar GTFS processing library)
- geopy (for geocoding)

See `requirements.txt` for full dependencies.

## 🎯 Technical Details

- **GTFS Processing**: Reads shapes.txt from GTFS feeds to plot transit routes
- **Buffer Calculation**: Creates 3/4 mile (1.207 km) buffers around all transit routes
- **Geocoding**: Uses address geocoding to pinpoint locations
- **Mapping**: Interactive Folium maps with OpenStreetMap tiles
- **Export**: Generates standalone HTML map files

## 🤝 Contributing

Contributions, issues, and feature requests are welcome! This tool is designed to help transit professionals, and community input helps make it better.

## 📝 License

This project is licensed under the Creative Commons Attribution 4.0 International License (CC BY 4.0) - see the [LICENSE](LICENSE) file for details.

## 👏 Credits

Created by Christian J Ferreira

## 📧 Contact

Christian J Ferreira - [LinkedIn](https://www.linkedin.com/in/christianjferreira/) - data@christianjferreira.com

Project Link: https://github.com/CJFData/RideFind

## 🔗 Related Resources

- [FTA ADA Regulations](https://www.transit.dot.gov/regulations-and-guidance/civil-rights-ada/ada-regulations)
- [GTFS Specification](https://gtfs.org/)
- [General Transit Feed Specification Reference](https://developers.google.com/transit/gtfs/reference)

---

⭐ If you found this tool helpful for your transit agency, please consider giving it a star!
