## Yearly Congestive Heart Failure Deaths vs. Air Quality Index Data


# Purpose
This project will compare yearly deaths from congestive heart failure with the average US air quality index measurements of PM2.5 levels.

High levels of PM2.5 have been linked with heart issues. 
Low AQI measurements indicate better air quality. 
An AQI measurement of 100 is considered unsafe.

While there should be a connection between higher concentrations of PM2.5 pollution and congestive heart failure deaths, this data does not show a correlation. This could be due to many things, with the most likely being that other factors have a larger effect on the numbers of congestive heart failure deaths than high PM2.5 levels, such as diet, environment, etc.


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

2. Install all requirements listed in "requirements.txt"

3. Open a cmd terminal in the "us-air-quality-vs-heart-failure-rates\.venv\Scripts" folder

4. Type the word "activate", and hit enter

5. Cd back to main folder and enter the command "python main.py"

6. The graphs should now be generated and saved in the main folder


# Notes
The original US_AQI.csv file had to be trimmed and converted to a pickle file before uploading because it was 600MB

The code used has been left commented in "main.py"

# Sources
A Kaggle dataset of US AQI data 1988-2022:
https://www.kaggle.com/datasets/calebreigada/us-air-quality-1980present?select=US_AQI.csv

The CDC Wonder Data Tool pulling cause of death statistics from 1999-2020, with results grouped by year and filtered for deaths caused by "Diseases of the circulatory system":
https://wonder.cdc.gov/controller/datarequest/D76