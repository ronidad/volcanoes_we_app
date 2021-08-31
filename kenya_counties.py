import folium
import pandas as pd

map = folium.Map([-1.289772712474131, 36.78426333871622], zoom_start=6,tiles= "Stamen Terrain")

folium.GeoJson(data=(open('json_data/counties.json','r', encoding="utf-8-sig").read())).add_to(map)


map.save("kenya.html")
