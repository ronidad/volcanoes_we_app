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
    folium.CircleMarker( location=[lt,ln], radius=6, popup=str(lv)+ " m " + nm, 
    fill_color= color_producer(lv), color="grey", fill_capacity=0.7).add_to(map)

folium.GeoJson(data=(open('json_data/world.json','r', encoding="utf-8-sig").read())).add_to(map)


map.save('maps.html')

