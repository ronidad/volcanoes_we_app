import folium
import pandas as pd


World_cordinates = pd.read_csv("world_coordinates.csv")
lat = list(World_cordinates["latitude"])
long = list(World_cordinates['longitude'])
country_code = list(World_cordinates["country_code"])

wmap=folium.Map([-0.023559,37.906193], zoom_start=6, tiles="Stamen Terrain")
for wlt,wln,wcode in zip(lat,long,country_code):
    folium.Marker(location=[wlt,wln],popup=wcode, icon=folium.Icon(color="red",icon="cloud") ).add_to(wmap)
wmap.save("world_map.html")