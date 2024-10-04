Nama: Indah Ayu Putri Mashita Cahyani
Email: indahmcshita.q@gmail.com
ID Dicoding: iapmashitac

# Air Quality Data Analysis Project Nongzhanguan Station

## Live Dashboard
[Air Quality Dashboard](https://air-quality-data-ah8mb8fas5nhry5ruses6w.streamlit.app/)

## Project Overview
This project, submitted for the "Learn Data Analysis with Python" course from Dicoding, focuses on analyzing air quality data, particularly PM2.5 levels, from the Nongzhanguan  station.

## Introduction
The goal of this project is to analyze air quality data, specifically PM2.5 pollutant levels, and understand their relationship with various environmental factors. The analysis includes identifying trends, seasonal patterns, and correlations with weather conditions.

## Data Source
The dataset used in this project includes air quality measurements from the Nongzhanguan station, with a focus on PM2.5 levels and other related environmental data.

## Libraries Used
- Streamlit
- Pandas
- Matplotlib
- Seaborn
- NumPy
- SciPy
- Statsmodels

## Key Insights
- Seasonal variation in PM2.5 levels with higher concentrations in colder months.
- Correlation between PM2.5 levels and weather conditions like temperature and humidity.
- Trends and patterns revealed through time series analysis.

## How to Run the Dashboard
To run the Air Quality Analysis Dashboard, follow these steps:

### Setup Environment
Create and Activate a Python Environment:

#### If using Conda (ensure Conda is installed):
```bash
conda create --name airquality-ds python=3.9
conda activate airquality-ds

If using venv (standard Python environment tool):
python -m venv airquality-ds
source airquality-ds/bin/activate  # On Windows use `airquality-ds\Scripts\activate`

Install Required Packages:
The following packages are necessary for running the analysis and the dashboard:
pip install pandas numpy scipy matplotlib seaborn streamlit statsmodels

Run the Streamlit App
Navigate to the Project Directory where dashboard/app.py is located.
streamlit run dashboard/app.py


The dataset used for this analysis is included in the project repository.
A detailed Python notebook (Indah_Notebook_Analisis_Data.ipynb) containing the data analysis and visualizations is also provided.

Note:
Since Dicoding recommended creating the good and tidy folder structures, as dashboard/app.py in the dashboard folder, then the deployment for Streamlit App affected.

Thats why I put the requirements.txt in the dashboard folder as well.