import streamlit as st
import matplotlib.pyplot as plt
import folium
from streamlit.components.v1 import html

st.title('COVID-19 Therapeutic Locator')

st.header("Data source")
st.write("""
HealthData.gov is the U.S. government's open data platform, managed by the Department of Health and 
Human Services (HHS) (Link: [HealthData.gov](https://healthdata.gov/stories/s/chu2-wqes)). It provides access to a vast 
array of health-related datasets, tools, and applications aimed at enhancing transparency and fostering 
innovation in healthcare.

The platform hosts thousands of datasets from various HHS agencies, covering topics such as health statistics, 
healthcare quality, and social determinants of health. These datasets are valuable resources for researchers, 
policymakers, and the public, facilitating data-driven decision-making and promoting public health initiatives.

For instance, HealthData.gov offers datasets like the "U.S. COVID-19 Self-Test Data," which includes self-test 
result data voluntarily reported by users through manufacturer websites and mobile applications.

By leveraging these datasets, users can gain insights into various health trends, disparities, and outcomes, 
contributing to a more informed and healthier society.
""")

#1. Top Metrics Section
st.header("Top Metrics")
st.write("Total Sites: 65468")
st.write("ICATT sites: 26")
st.write("Home Delivery Sites: 325")
st.write("Prescribing Services Available: 534")

#2. Medication Availability
st.header("Medication Availability")
st.image("./data/images/medication_availability.png")

#3. Service Accessibility Pie chart
st.header("Service Availability")
st.image("./data/images/service_availability.png")

#4. Change in proportion of over time
st.header("Proportion of active sites")
st.image("./data/images/closed_sites.png")


#5.Medication availability over time
st.header("Medication Availability Over Time")
st.image("./data/images/medication_availability_over_time.png")

#6.Number of medication sites
st.header("States with Medication Sites")
st.image("data/images/number_of_treatment_sites.png")

#7. Geospatial Analysis: Interactive Map
map_file = "data/geospatial_data/medication_sites_map_with_dropdown.html"

with open(map_file, 'r', encoding='utf-8') as f:
    map_html = f.read()
    
st.title("Interactive Medication Sites Map")
st.write("Explore the distribution of treatment sites on the map.\nUse the dropdown menu on the right corner to choose the treatment site")
st.write("To see the address of the treatment site, click on the treatment site point.")
st.write("")

html(map_html, height=600)