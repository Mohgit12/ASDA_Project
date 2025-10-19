# ASDA_Project

🌿 **Natura2000 Coverage Dashboard**

This is an interactive Streamlit dashboard to visualize Natura2000 coverage by municipality. Users can select a municipality, see its coverage percentage, compare coverage across municipalities, and view the location on an interactive map.

## Features

- Select a municipality from a dropdown menu
- Display Natura2000 coverage (%) for the selected municipality
- Bar chart showing coverage across municipalities with the highest percenatges
- Interactive map highlighting the selected municipality

## Installation 

1. Clone the Repository:
```
git clone https://github.com/<your-username>/ASDA_Project.git
cd ASDA_Project
```
2. Creating and Activating a Python Environment (Optional): 
```
python -m venv venv
```
On Windows
```
venv\Scripts\activate
```
On Mac/Linux
```
source venv/bin/activate
```

3. Install Required Packages:
```
pip install pandas geopandas streamlit folium streamlit-folium
```

## Usage
```
streamlit run natura_dashboard.py
```
## Data
Percentages_Natura2000.csv: Contains municipality-level Natura2000 coverage percentages. 

Municipalities.gpkg: GeoPackage file with municipality boundaries.

## Notes
- Make sure you are running the code using your Python environment or Jupyter kernel
`pip/conda activate env_name`
- Navigate to the folder where natura_dashboard.py is located before running the command.
- If the file name does not work, provide the full path to the script instead:
`streamlit run "C:\Users\YourName\Path\To\Project\natura_dashboard.py"` for example



