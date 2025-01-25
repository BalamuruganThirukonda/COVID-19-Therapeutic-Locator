import pandas as pd
import folium
from folium.plugins import MarkerCluster



df = pd.read_csv("./data/raw_data/clinical_data.csv")


# Filter for Paxlovid and Lagevrio sites
paxlovid_sites = df[df['Has Paxlovid'] == True]
lagevrio_sites = df[df['Has Lagevrio'] == True]
veklury_site = df[df['Has Veklury'] == True]
baloxavir_site = df[df['Has Baloxavir'] == True]
commercial_lagevrio_site = df[df['Has Commercial Lagevrio'] == True]
commercial_paxlovid_site = df[df['Has Commercial Paxlovid'] == True]
oseltamivir_generic_site = df[df['Has Oseltamivir Generic'] == True]
oseltamivir_suspension_site = df[df['Has Oseltamivir Suspension'] == True]
peramvir_site = df[df['Has Peramivir'] == True]
oseltamivir_tamiflu_site = df[df['Has Oseltamivir Tamiflu'] == True]
usg_paxlovid_site = df[df['Has USG Paxlovid'] == True]
usg_lagevrio_site = df[df['Has USG Lagevrio'] == True]
zanamivir_site = df[df['Has Zanamivir'] == True]
home_delivery_site = df[df['Home Delivery'] == True]

# Create the map
mymap = folium.Map(location=[37.0902, -95.7129], zoom_start=4)

# Create MarkerCluster
paxlovid_cluster = MarkerCluster(name="Paxlovid Sites").add_to(mymap)
lagevrio_cluster = MarkerCluster(name='Lagevrio Sites').add_to(mymap)
veklury_cluster = MarkerCluster(name='Veklury Sites').add_to(mymap)
baloxavir_cluster = MarkerCluster(name="Baloxavir Sites").add_to(mymap)
commercial_lagevrio_cluster = MarkerCluster(name="Commercial Lagevrio Sites").add_to(mymap)
commercial_paxlovid_cluster = MarkerCluster(name='Commercial Paxlovid Sites').add_to(mymap)
oseltamivir_generic_cluster = MarkerCluster(name='Oseltamivir Generic Sites').add_to(mymap)
oseltamivir_suspension_cluster = MarkerCluster(name='Oseltamivir Suspension Sites').add_to(mymap)
peramvir_cluster = MarkerCluster(name='Has Peramivir Sites').add_to(mymap)
oseltamivir_tamiflu_cluster = MarkerCluster(name='Oseltamivir Tamiflu Sites').add_to(mymap)
usg_paxlovid_cluster = MarkerCluster(name='USG Paxlovid Sites').add_to(mymap)
usg_lagevrio_cluster = MarkerCluster(name='USG Lagevrio Sites').add_to(mymap)
zanamivir_cluster = MarkerCluster(name='Zanamivir Sites').add_to(mymap)
home_delivery_cluster = MarkerCluster(name='Home Delivery').add_to(mymap)


# Add markers for Paxlovid
for _, row in paxlovid_sites.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=5,
        color="blue",
        fill=True,
        fill_color="blue",
        fill_opacity=0.6,
        popup=f"Site: {row['Geopoint']}<br>Address: {row['Address 1']}<br>City: {row['City']}<br>State:{row['State']}<br>Last Report:{row['Last Report Date']}",
    ).add_to(paxlovid_cluster)

# Add markers for Lagevrio (change color)
for _, row in lagevrio_sites.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=5,
        color="green",
        fill=True,
        fill_color="green",
        fill_opacity=0.6,
        popup=f"Site: {row['Geopoint']}<br>Address: {row['Address 1']}<br>City: {row['City']}<br>State:{row['State']}<br>Last Report:{row['Last Report Date']}",
    ).add_to(lagevrio_cluster)

# Add markers for Veklury
for _, row in veklury_site.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=5,
        color="red",
        fill=True,
        fill_color="red",
        fill_opacity=0.6,
        popup=f"Site: {row['Geopoint']}<br>Address: {row['Address 1']}<br>City: {row['City']}<br>State:{row['State']}<br>Last Report:{row['Last Report Date']}",
    ).add_to(veklury_cluster)

# Add markers for Baloxavir
for _, row in baloxavir_site.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=5,
        color="purple",
        fill=True,
        fill_color="purple",
        fill_opacity=0.6,
        popup=f"Site: {row['Geopoint']}<br>Address: {row['Address 1']}<br>City: {row['City']}<br>State:{row['State']}<br>Last Report:{row['Last Report Date']}",
    ).add_to(baloxavir_cluster)

# Add markers for Commercial Lagevrio
for _, row in commercial_lagevrio_site.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=5,
        color="green",
        fill=True,
        fill_color="green",
        fill_opacity=0.6,
        popup=f"Site: {row['Geopoint']}<br>Address: {row['Address 1']}<br>City: {row['City']}<br>State:{row['State']}<br>Last Report:{row['Last Report Date']}",
    ).add_to(commercial_lagevrio_cluster)
    
for _,row in commercial_paxlovid_site.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=5,
        color="blue",
        fill=True,
        fill_color="blue",
        fill_opacity=0.6,
        popup=f"Site: {row['Geopoint']}<br>Address: {row['Address 1']}<br>City: {row['City']}<br>State:{row['State']}<br>Last Report:{row['Last Report Date']}",        
    ).add_to(commercial_paxlovid_cluster)

for _,row in oseltamivir_generic_site.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=5,
        color="orange",
        fill=True,
        fill_color="orange",
        fill_opacity=0.6,
        popup=f"Site: {row['Geopoint']}<br>Address: {row['Address 1']}<br>City: {row['City']}<br>State:{row['State']}<br>Last Report:{row['Last Report Date']}",
    ).add_to(oseltamivir_generic_cluster)
    
for _,row in oseltamivir_suspension_site.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=5,
        color='gray',
        fill=True,
        fill_color="gray",
        fill_opacity=0.6, 
        popup=f"Site: {row['Geopoint']}<br>Address: {row['Address 1']}<br>City: {row['City']}<br>State:{row['State']}<br>Last Report:{row['Last Report Date']}",
    ).add_to(oseltamivir_suspension_cluster)
        
for _,row in peramvir_site.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=5,
        color="brown",
        fill=True,
        fill_color="brown",
        fill_opacity=0.6,
        popup=f"Site: {row['Geopoint']}<br>Address: {row['Address 1']}<br>City: {row['City']}<br>State:{row['State']}<br>Last Report:{row['Last Report Date']}",        
    ).add_to(peramvir_cluster)
    
for _,row in oseltamivir_tamiflu_site.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=5,
        color="cyan",
        fill=True,
        fill_color="cyan",
        fill_opacity=0.6,
        popup=f"Site: {row['Geopoint']}<br>Address: {row['Address 1']}<br>City: {row['City']}<br>State:{row['State']}<br>Last Report:{row['Last Report Date']}",        
    ).add_to(oseltamivir_tamiflu_cluster)
    
for _,row in usg_paxlovid_site.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=5,
        color="blue",
        fill=True,
        fill_color="blue",
        fill_opacity=0.6,
        popup=f"Site: {row['Geopoint']}<br>Address: {row['Address 1']}<br>City: {row['City']}<br>State:{row['State']}<br>Last Report:{row['Last Report Date']}",        
    ).add_to(usg_paxlovid_cluster)
    
for _, row in usg_lagevrio_site.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=5,
        color="green",
        fill=True,
        fill_color="green",
        fill_opacity=0.6,
        popup=f"Site: {row['Geopoint']}<br>Address: {row['Address 1']}<br>City: {row['City']}<br>State:{row['State']}<br>Last Report:{row['Last Report Date']}",
    ).add_to(usg_lagevrio_cluster)
    
for _, row in zanamivir_site.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=5,
        color="pink",
        fill=True,
        fill_color="pink",
        fill_opacity=0.6,
        popup=f"Site: {row['Geopoint']}<br>Address: {row['Address 1']}<br>City: {row['City']}<br>State:{row['State']}<br>Last Report:{row['Last Report Date']}",
    ).add_to(zanamivir_cluster)
    
for _, row in home_delivery_site.iterrows():
    folium.CircleMarker(
        location=[row['Latitude'], row['Longitude']],
        radius=5,
        color="green",
        fill=True,
        fill_color="green",
        fill_opacity=0.6,
        popup=f"Site: {row['Geopoint']}<br>Address: {row['Address 1']}<br>City: {row['City']}<br>State:{row['State']}<br>Last Report:{row['Last Report Date']}",
    ).add_to(home_delivery_cluster)
    
       
folium.LayerControl().add_to(mymap)

# Save the map
mymap.save("medication_sites_map_with_dropdown.html")
