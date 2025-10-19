import pandas as pd
import streamlit as st
import geopandas as gpd
import folium
from streamlit_folium import st_folium

# Load data

df = pd.read_csv(r"Percentages_Natura2000.csv")  
gdf = gpd.read_file(r"Municipalities.gpkg")  
gdf = gdf.to_crs(epsg=4326)  # Ensure WGS84 for Folium

# Streamlit layout

st.title("🌿 Natura2000 Coverage by Municipality")

# Municipality dropdown
municipalities = df['naam'].sort_values().unique()
selected_mun = st.selectbox("Select a municipality:", municipalities)

# Display metric

pct_natura = df.loc[df['naam'] == selected_mun, 'pct_natura'].values[0]
st.metric(label="Natura2000 coverage (%)", value=f"{pct_natura:.2f}")

# Bar chart

st.subheader("Coverage by Municipality")
st.bar_chart(df.sort_values('pct_natura', ascending=False).set_index('naam')['pct_natura'])


# Map

st.subheader("Municipality Map")

# Filter selected municipality
selected_gdf = gdf[gdf['naam'] == selected_mun]

# Center map on selected municipality
centroid = selected_gdf.geometry.centroid.iloc[0]
m = folium.Map(location=[centroid.y, centroid.x], zoom_start=10)

# Draw all municipalities in light grey
folium.GeoJson(
    gdf,
    style_function=lambda x: {
        "fillColor": "lightgrey",
        "color": "white",
        "weight": 0.5,
        "fillOpacity": 0.5
    },
    tooltip=folium.GeoJsonTooltip(fields=["naam"], aliases=["Municipality:"])
).add_to(m)

# Highlight selected municipality in red outline
folium.GeoJson(
    selected_gdf,
    style_function=lambda x: {
        "fillColor": "none",
        "color": "red",
        "weight": 3,
        "fillOpacity": 0.8
    },
    tooltip=folium.GeoJsonTooltip(fields=["naam"], aliases=["Selected Municipality:"])
).add_to(m)

# Display interactive map
st_folium(m, width=700, height=500)