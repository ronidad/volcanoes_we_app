import folium
from folium.map import Icon, Popup




office = [-1.2897190818854458, 36.783920015980534]
home= [-1.3433738618892992, 36.98445237479201]
water = [-1.506969, 36.934364]
map = folium.Map(office, zoom_start=10,tiles= "Stamen Terrain")

#folium.LayerControl().add_to(map) 
#map.add_child(folium.Marker(location=[33.4, -7.5]), popup="Hi, I am a marker", icon=folium.Icon(color="green"))
for cordinate in [home, water]:
    maker_name = [k for k, v in locals().items() if v == cordinate][0] 
 
    folium.Marker( location=cordinate, popup=maker_name, icon=folium.Icon(color='green', icon="cloud") ).add_to(map)




map.save('map.html')