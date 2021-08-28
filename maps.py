import folium
import pandas as pd


data = pd.read_csv("volcanoes.txt")
lat= list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map([38.58,-99.89], zoom_start=6,tiles= "Stamen Terrain")
for lt,ln,lv in zip(lat, lon,elev):
    folium.Marker( location=[lt,ln], popup=str(lv), icon=folium.Icon(color='green', icon="cloud") ).add_to(map)
map.save('maps.html')


World_cordinates = pd.read_csv("world_coordinates.csv")
wlat = list(World_cordinates["latitude"])
wlong = list(World_cordinates['longitude'])
country_code = list(World_cordinates["country_code"])

wmap=folium.Map([-0.023559,37.906193], zoom_start=6, tiles="Stamen Terrain")
for wlt,wln,wcode in zip(wlat,wlong,country_code):
    folium.Marker(location=[wlt,wln],popup=wcode, icon=folium.Icon(color="red",icon="cloud") ).add_to(wmap)
wmap.save("world_map.html")