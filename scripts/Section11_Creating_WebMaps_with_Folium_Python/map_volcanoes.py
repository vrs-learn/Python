##
### Map the Volcanoes
##

import folium
import pandas

volcanoes = pandas.read_csv("Volcanoes_USA.txt")
vol_names = volcanoes.loc[:,"NAME"]
vol_lat = volcanoes.loc[:,"LAT"]
vol_lon = volcanoes.loc[:,"LON"]
vol_elev = volcanoes["ELEV"]
#print(volcanoes)

def color_producer(elev):
    if elev < 1000 :
        return 'green'
    elif 1000 <= elev < 3000 :
        return 'orange'
    else :
        return 'red'

map = folium.Map(location=[0,0])

fg = folium.FeatureGroup(name="My Map")

for name,lat,lon,elev in zip(vol_names,vol_lat,vol_lon,vol_elev):
    #print(type(name))
    name = name +" , Elev: " + str(elev) + "m"
    #fg.add_child(folium.Marker(location=[lat,lon], popup=folium.Popup(name,parse_html=True), icon=folium.Icon(color=color_producer(elev))))    # this is for using simple Marker
    fg.add_child(folium.CircleMarker(location=[lat,lon], popup=folium.Popup(name,parse_html=True), fill="true", fill_color=color_producer(elev), color = 'grey'))  # this is for using Circle Marker
    print(name,lat,lon)

map.add_child(fg)

map.save("VolcanoesMap.html")
