Hello!

RideFind is designed to help transit professionals identify if a start or end of a trip is within the 3/4 mile ADA zone. Whether a trip starts or ends in the 3/4 zone buffer is used for ADA program requirements. it uses Python with the Streamlit Library for the webapp interface, and Folium for the interactive map. Map shapes are uploaded from public GTFS files

First Run Libraryinstall.py to install the necessary libraries to run this. (If you already have all dependencies installed you will not need to run this)
Then save and Ridefind.py which will initialize the Streamlit webapp on your system.
Then Run !streamlit run RideFind.py --server.headless true (RunServer.py) to run the app. 

It may be easier to save each of these files as codeblocks in a Jupyter notebook instead.

1. Upload your GTFS file
<img width="1385" height="515" alt="image" src="https://github.com/user-attachments/assets/93b157fb-611d-49e6-a3f7-c723d1ee2cd6" />

2. Search the address, if you don't know the full address the app will attempt to autocomplete it, and you can select an option from the dropdown, 
be sure to at least have street address and town.
<img width="1454" height="380" alt="image" src="https://github.com/user-attachments/assets/ce30fb06-f9db-48b4-8e67-a57e04f7b439" />

3. Click 'Show On Map' and it will plot the Transit network from GTFS and show where the address you searched sits on the map with a green pin

<img width="1546" height="978" alt="image" src="https://github.com/user-attachments/assets/6fa522f2-43d4-479f-abe1-755575b88fc9" />

Once you are done, you can download this mapped image by clicking 'Download HTML Map'

<img width="1014" height="487" alt="image" src="https://github.com/user-attachments/assets/8f801b28-fc25-4281-a4ff-4c6847313f52" />

