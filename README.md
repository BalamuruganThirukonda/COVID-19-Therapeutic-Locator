# COVID-19-Therapeutic-Locator
# Data source
HealthData.gov is the U.S. government's open data platform, managed by the Department of Health and Human Services (HHS) (Link: HealthData.gov). It provides access to a vast array of health-related datasets, tools, and applications aimed at enhancing transparency and fostering innovation in healthcare.

The platform hosts thousands of datasets from various HHS agencies, covering topics such as health statistics, healthcare quality, and social determinants of health. These datasets are valuable resources for researchers, policymakers, and the public, facilitating data-driven decision-making and promoting public health initiatives.

For instance, HealthData.gov offers datasets like the "U.S. COVID-19 Self-Test Data," which includes self-test result data voluntarily reported by users through manufacturer websites and mobile applications.

By leveraging these datasets, users can gain insights into various health trends, disparities, and outcomes, contributing to a more informed and healthier society.

# Folder Structure
COVID-19-Therapeutic-Locator/
│
├── data/
│   ├── raw_data/                  # Raw input data (unaltered)
│   ├── geospatial_data/           # Contains interactive map .html file
│   └── images/                    # Contains plots
│
├── src/
│   ├── clinical_data.ipynb        # EDA Jupiter file
│   ├── medication_distribution.py # Script for interactive map
│
├── LICENCE                        # MIT license
├── requirements.txt               # Dependencies required to run the project
├── README.md                      # Project overview and instructions
├── dashboard.py                   # Script for Streamlit app
└── .gitignore                     # Files and folders to exclude from version control

# Getting Started
## Clone the Repository
  git clone https://github.com/your_username/diabetes-predictions.git
  cd diabetes-predictions

## Set Up a Virtual Environment
  python -m venv env
  source env/bin/activate  # On Windows: `env\Scripts\activate`

## Install Dependencies
  pip install -r requirements.txt

# Prerequisites
Python 3.8+
Jupyter Notebook
Libraries specified in requirements.txt

# License
This project is licensed under the MIT License. Feel free to use and modify it with proper attribution.

This README provides clarity and a structured overview for users, ensuring they can easily navigate and utilize the repository effectively
