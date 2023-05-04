import pandas as pd

# Extract data from a CSV file
data = pd.read_csv('raw_data.csv')

# Remove any rows with missing values
data.dropna(inplace=True)

# Convert the 'date' column to a datetime object
data['fecha_hecho'] = pd.to_datetime(data['fecha_hecho'])

# Write the transformed data to a new CSV file
data.to_csv('cleaned_raw_data.csv', index=False)

# Extract datas from a new CSV file
data1 = pd.read_csv('cleaned_raw_data.csv')

# Load a data set like a json file
data1.to_json('cleaned_raw_data.json')
