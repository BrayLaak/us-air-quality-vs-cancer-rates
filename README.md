## Yearly Congestive Heart Failure Deaths vs. Air Quality Index Data


# Purpose
This project will compare yearly deaths from congestive heart failure with the average US air quality index measurements of PM2.5 levels.


# Explanation

High levels of Particle Matter 2.5 (PM2.5) have been linked with heart issues. 

Low air quality index (AQI) measurements indicate better air quality. 

An AQI measurement of 100 is considered unsafe.

This project takes averaged data on AQI measurements from across the US that use measurements of PM2.5 levels and compares it with avereaged yearly deaths from congestive heart failure in the US.

The first graph generated shows the trend in AQI measurements from 1988-2022. The second graph shows the trends in congestive heart failure deaths from 1999-2020. Finally, the third graph shows both trends combined and trimmed to only show the years included in each dataset.

To discuss the findings, the comparison graph does not show the correlation expected given the science on PM2.5 levels and heart issues. This could be due to many things, with the most likely being that other factors have a larger effect on the numbers of congestive heart failure deaths than high PM2.5 levels, such as diet, environment, etc.


# Features

This project will: 

Pull in data from csv and tab delineated txt files gathered from the sources cited below

Use built-in pandas functions to clean the data

Use custom functions to operate on the data

Make 2 basic plots with matplotlib to visualize the data from each dataset and output the graphs to the following files: 

>"AQI Readings.pdf"

>"CHF Deaths.pdf"

Combine the dataframes, plot the data on one graph for comparison, and output the graph to the following file:

>"Combined Graph.pdf"


# Instructions
This project was created in Python 3.10.4
1. Clone the repository to your local machine.

2. Install all requirements listed in "requirements.txt". If this fails, pip install matplotlib and pandas

3. Open a cmd terminal in the "us-air-quality-vs-heart-failure-rates\.venv\Scripts" folder

4. Run main.py

6. The graphs should now be generated and saved in the main folder


# Notes
The original US_AQI.csv file had to be trimmed and converted to a pickle file before uploading because it was 600MB

This is the orignal code used:
>aqi_data = pd.read_csv("US_AQI.csv")

> aqi_data = aqi_data.drop(aqi_data.columns[[0, 1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14]], axis=1)

>aqi_data = aqi_data.loc[aqi_data['Defining Parameter'] == 'PM2.5']

>aqi_data.to_pickle('US_AQI.pkl')


# Sources
A Kaggle dataset of US AQI data 1988-2022:
https://www.kaggle.com/datasets/calebreigada/us-air-quality-1980present?select=US_AQI.csv

The CDC Wonder Data Tool pulling cause of death statistics from 1999-2020, with results grouped by year and filtered for deaths caused by "Diseases of the circulatory system":
https://wonder.cdc.gov/controller/datarequest/D76