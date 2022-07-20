import pandas as pd

# Code to trim the original US_AQI.csv file before uploading because it was 600MB 
#aqi_data = pd.read_csv("US_AQI.csv")
#aqi_data = aqi_data.drop(aqi_data.columns[[0, 1, 4, 6, 7, 8, 9, 10, 11, 12, 13, 14]], axis=1)
#aqi_data = aqi_data.loc[aqi_data['Defining Parameter'] == 'PM2.5']
#aqi_data.to_csv(r'C:/Users/Brayden/Documents/GitHub/us-air-quality-vs-heart-failure-rates/data/data.csv', index = False)

aqi_data = pd.read_csv("US_AQI.csv")

aqi_data['Date'] = pd.to_datetime(aqi_data['Date'])
aqi_data['Year'] = aqi_data['Date'].dt.year
aqi_data = aqi_data.drop(aqi_data.columns[[0, 2]], axis=1)

aqi_data.head()


#chf_data = pd.read_csv('heart_failure_stats.txt', sep='/t', lineterminator='/r')
#chf_data = chf_data.loc[chf_data['Cause of death'] == 'Congestive heart failure']
#chf_data = chf_data.drop(chf_data.columns[[0, 2, 3, 4, 6, 7]], axis=1)
#chf_data = chf_data.astype({"Year": int, "Deaths": int})
#chf_data.head()



