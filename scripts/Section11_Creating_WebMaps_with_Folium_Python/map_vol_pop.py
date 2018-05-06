import folium
import pandas

volcanoes = pandas.read_csv("Volcanoes_USA.txt")
vol_names = list(volcanoes["NAME"])
vol_lat = list(volcanoes["LAT"])
vol_lon = list(volcanoes["LON"])
vol_elev = list(volcanoes["ELEV"])
#print(volcanoes)

def color_producer(elev):
    if elev < 1000 :
        return 'green'
    elif 1000 <= elev < 3000 :
        return 'orange'
    else :
        return 'red'

map = folium.Map(location=[0,0], zoom_start=6, tiles="Mapbox Bright")

fgv = folium.FeatureGroup(name="Volcanoes")

for name,lat,lon,elev in zip(vol_names,vol_lat,vol_lon,vol_elev):
    #print(type(name))
    name = name +" , Elev: " + str(elev) + "m"
    fgv.add_child(folium.CircleMarker(location=[lat,lon], radius=6, popup=folium.Popup(name,parse_html=True), fill="true", fill_color=color_producer(elev), color = 'grey'))  # this is for using Circle Marker
    print(name,lat,lon)

fgp = folium.FeatureGroup(name="Population")

fgp.add_child(folium.GeoJson(data=open('world.json','r', encoding='utf-8-sig').read() ,
style_function=lambda x: {'fillColor':'green' if x['properties']['POP2005'] < 10000000
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red' }))

map.add_child(fgv)
map.add_child(fgp)

map.add_child(folium.LayerControl()) # Make sure to add this layer after the feature group

map.save("VolcanoesMap1.html")
