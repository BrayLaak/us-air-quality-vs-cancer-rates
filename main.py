import pandas as pd
from matplotlib import pyplot as plt


# Function to remove rows with NAN values from dataframe
def remove_NAN_rows(df):
    return df.dropna()

# Function to generate a simple line graph, add a grid, and save the graph to a file
def generate_graph(df, xAxis, yAxis, graph_title, graph_color):
    df_graph = df.plot(x=xAxis, y=yAxis, title=graph_title, color=graph_color)
    df_graph.grid()
    df_graph.figure.savefig(graph_title + '.pdf')
    return



# Read in AQI data pickle
aqi_data = pd.read_pickle("US_AQI.pkl")

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

# Create AQI Readings graph by calling custom function
generate_graph(aqi_data, 'Year', 'AQI', 'AQI Readings from 1988-2022', 'red')



#read in CHF data tab delineated txt file and remove header row
chf_data = pd.read_csv('heart_failure_stats.txt', sep='\t', lineterminator='\r', header=[0])

# Filter out all rows with other causes of death and update chf_data with cleaned rows
chf_data = chf_data.loc[chf_data['Cause of death'] == 'Congestive heart failure']

# Drop unnecessary columns
chf_data = chf_data.drop(chf_data.columns[[0, 2, 3, 4, 6, 7]], axis=1)

# Change column types to int
chf_data = chf_data.astype({"Year": int, "Deaths": int})

# Create Yearly CHF Deaths graph by calling custom function
generate_graph(chf_data, 'Year', 'Deaths', 'Yearly CHF Deaths from 1999-2020', 'green')



# Merge dataframes on Year, create new merged dataframe
merged_data = aqi_data.merge(chf_data, on='Year', how='outer')

# Drop any rows with NAN values to trim the dataframe down to only years that both columns have data for
merged_data = remove_NAN_rows(merged_data)


# Begin creating subplots for each data column
fig, ax = plt.subplots()

# Plot AQI, set tick labels to the same color, set labels, and set legend
ax.plot(merged_data['Year'], merged_data['AQI'], color='red')
ax.tick_params(axis='y', labelcolor='red')
ax.set_ylabel('AQI',  color='red', fontsize=15)
ax.set_xlabel('Year')


# Generate a new axis instance to use for CHF data
ax2 = ax.twinx()

# Plot congestive heart failure deaths, change tick color, set labels, and set legend
ax2.plot(merged_data['Year'], merged_data['Deaths'], color='green')
ax2.tick_params(axis='y', labelcolor='green')
ax2.set_ylabel('CHF Deaths',  color='green', fontsize=15)
ax2.set_xlabel('Year')


# Add title and grid to graph, then scale output
plt.title(label='AQI and Yearly CHF Deaths from 1999-2020')
plt.grid()
fig.set_tight_layout(True)

# Save graph to file
fig.figure.savefig('Combined Graph.pdf')