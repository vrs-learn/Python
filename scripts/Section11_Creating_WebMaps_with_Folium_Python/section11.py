###################
#### Working with folium
#### Folium converts the python code into html, css & java script.
###################

import folium

dir(folium)
help(folium.Map)

map = folium.Map(location=[18.456, 73.91], zoom_start=6, tiles="Mapbox Bright") # location is in Latitude & Longitude . Latitude range is from -90 to 0 to 90. Longitude goes from -180 to 0 to 180
# zoom_start is to set the zoom of the map.
# tiles is the background of the map. THat can be set as you need.
map.save("Map1.html")

##################
# Adding point markers.
# We need to add an object to an existing map.
##################

map = folium.Map(location=[18.456, 73.91], zoom_start=6, tiles="Mapbox Bright")
# After creating the Map object and saving it, the new objects ( of creating Markers ) should be added in between.
map.add_child(folium.Marker(location=[18.4, 73.9], popup="UNDRI BLISS", icon=folium.Icon(color='green')))
map.save("Map1.html")

# Another better way of adding Marker is by using the Feature Group
#
map = folium.Map(location=[18.456, 73.91], zoom_start=6, tiles="Mapbox Bright")
fg=folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[18.4, 73.9], popup="UNDRI BLISS", icon=folium.Icon(color='green')))
map.add_child(fg)

map.save("Map1.html")

#########################
### For Adding multiple co-ordinates , we can use a For Loop
#########################

map = folium.Map(location=[18.456, 73.91], zoom_start=6, tiles="Mapbox Bright")
fg=folium.FeatureGroup(name="My Map")

for coordinates in [[18.41, 73.911],[18.42, 73.92]]:
    fg.add_child(folium.Marker(location=coordinates, popup="UNDRI BLISS", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")

#############################################
### See Python script map_worldpopulation.py for Checking the GeoJson which is able to read the World Data based on JSON.
#############################################

####
#### For adding a Layer Control
#use :
#map.add_child(folium.LayerControl())
# for example check map_vol_pop.py
