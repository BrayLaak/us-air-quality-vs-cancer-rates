import pandas as pd
from matplotlib import pyplot as plt



# Code to trim the original US_AQI.csv file before uploading because it was 600MB 

#aqi_data = pd.read_csv("US_AQI.csv")
#aqi_data = aqi_data.drop(aqi_data.columns[[0, 1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14]], axis=1)
#aqi_data = aqi_data.loc[aqi_data['Defining Parameter'] == 'PM2.5']
#aqi_data.to_csv(r'C:/Users/Brayden/Documents/GitHub/us-air-quality-vs-heart-failure-rates/data/data.csv', index = False)



# Read in AQI data csv and remove header row
aqi_data = pd.read_csv("US_AQI.csv", header=[0])

# Change "Date" column to datetime
aqi_data['Date'] = pd.to_datetime(aqi_data['Date'])

# Simplify all dates to only show year
aqi_data['Year'] = aqi_data['Date'].dt.year

# Drop unnecessary columns
aqi_data = aqi_data.drop(aqi_data.columns[[0, 2]], axis=1)

# Calculate the average AQI per year, update aqi_data, and reset the index
aqi_data = aqi_data.groupby(['Year'], as_index=False)['AQI'].mean()
aqi_data = aqi_data.reset_index(drop=True)

# Round off AQI data to one decimal
aqi_data = aqi_data.round(1)




#read in CHF data tab delineated txt file and remove header row
chf_data = pd.read_csv('heart_failure_stats.txt', sep='\t', lineterminator='\r', header=[0])

# Filter out all rows with other causes of death and update chf_data with cleaned rows
chf_data = chf_data.loc[chf_data['Cause of death'] == 'Congestive heart failure']

# Drop unnecessary columns
chf_data = chf_data.drop(chf_data.columns[[0, 2, 3, 4, 6, 7]], axis=1)

# Change column types to int
chf_data = chf_data.astype({"Year": int, "Deaths": int})

# Merge dataframes on Year create new merged dataframe
merged_data = aqi_data.merge(chf_data, on='Year', how='outer')

# Drop any rows with NAN values to trim the dataframe down to only years that both columns have data for
merged_data = merged_data.dropna()


# Begin creating subplots for each data column
fig, ax = plt.subplots()

# Plot AQI, set tick labels to the same color, and set label
ax.plot(merged_data['Year'], merged_data['AQI'], color='red')
ax.tick_params(axis='y', labelcolor='red')
ax.set_ylabel('AQI',  color='red', fontsize=15)


# Generate a new axis instance to use for CHF data
ax2 = ax.twinx()

# Plot congestive heart failure deaths, change tick color, and set label
ax2.plot(merged_data['Year'], merged_data['Deaths'], color='green')
ax2.tick_params(axis='y', labelcolor='green')
ax2.set_ylabel('CHF Deaths',  color='green', fontsize=15)

# Add title, legend, xlabel, and grid to graph
plt.title(label='AQI and Yearly CHF Deaths')
plt.legend(['AQI', 'CHF Deaths'])

plt.xlabel('Year')
plt.grid()

plt.show()