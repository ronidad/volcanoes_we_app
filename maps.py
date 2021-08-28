import folium
import pandas as pd


data = pd.read_csv("volcanoes.txt")
lat= list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])
name= list(data['NAME'])


def color_producer(elevation):
    if elevation<1000:
        return "green"
    elif 1000<=elevation <=3000:
        return "orange"
    else:
        return "red"


map = folium.Map([34.7999992,-108.0009995], zoom_start=6,tiles= "Stamen Terrain",max_lat=33,max_lon=107,max_bounds=False)
for lt,ln,lv,nm in zip(lat, lon,elev,name):
    folium.Marker( location=[lt,ln], popup=str(lv)+ " meters " + nm, icon=folium.Icon(color=color_producer(lv), icon="cloud") ).add_to(map)
map.save('maps.html')


World_cordinates = pd.read_csv("world_coordinates.csv")
wlat = list(World_cordinates["latitude"])
wlong = list(World_cordinates['longitude'])
country_code = list(World_cordinates["country_code"])

wmap=folium.Map([-0.023559,37.906193], zoom_start=6, tiles="Stamen Terrain")
for wlt,wln,wcode in zip(wlat,wlong,country_code):
    folium.Marker(location=[wlt,wln],popup=wcode, icon=folium.Icon(color="red",icon="cloud") ).add_to(wmap)
wmap.save("world_map.html")