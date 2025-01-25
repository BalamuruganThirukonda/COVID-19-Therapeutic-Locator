import streamlit as st
import os
from streamlit.components.v1 import html

st.title('COVID-19 Therapeutic Locator')

# Data Source Section
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

# Function to Display Images with Error Handling
def display_image(image_path, alt_text):
    if os.path.exists(image_path):
        st.image(image_path)
    else:
        st.error(f"Image not found: {alt_text}")

# Function to Display Maps with Error Handling
def display_map(map_path):
    if os.path.exists(map_path):
        with open(map_path, 'r', encoding='utf-8') as f:
            map_html = f.read()
        html(map_html, height=600)
    else:
        st.error("Map file not found. Please check the file path.")

# 1. Top Metrics Section
st.header("Top Metrics")
st.write("- **Total Sites:** 65,468")
st.write("- **ICATT Sites:** 26")
st.write("- **Home Delivery Sites:** 325")
st.write("- **Prescribing Services Available:** 534")

# 2. Medication Availability
st.header("Medication Availability")
display_image("data/images/medication_availability.png", "Medication Availability Image")

# 3. Service Accessibility Pie Chart
st.header("Service Availability")
display_image("data/images/service_availability.png", "Service Availability Image")

# 4. Change in Proportion Over Time
st.header("Proportion of Active Sites")
display_image("data/images/closed_sites.png", "Proportion of Active Sites Over Time Image")

# 5. Medication Availability Over Time
st.header("Medication Availability Over Time")
display_image("data/images/medication_availability_over_time.png", "Medication Availability Over Time Image")

# 6. Number of Medication Sites
st.header("States with Medication Sites")
display_image("data/images/number_of_treatment_sites.png", "Number of Treatment Sites Image")

# 7. Geospatial Analysis: Interactive Map
st.header("Interactive Medication Sites Map")
st.write("Explore the distribution of treatment sites on the map. Use the dropdown menu on the right corner to choose the treatment site.")
st.write("To see the address of the treatment site, click on the treatment site point.")
display_map("data/geospatial_data/medication_sites_map_with_dropdown.html")
