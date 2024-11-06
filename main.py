from sklearn.preprocessing import MinMaxScaler
import pandas as pd
import numpy as np

filepath = '/Users/priyankaasurisetty/Desktop/BostonHousing.csv'

# Load the data
data = pd.read_csv(filepath)

# Replace missing values in the 'rm' column with the mean of 'rm'
data['rm'] = data['rm'].fillna(data['rm'].mean())

# Initialize MinMaxScaler
scaler = MinMaxScaler()

columns_to_scale = ['crim', 'zn', 'indus', 'rm', 'age', 'dis', 'rad', 'tax', 'ptratio', 'b', 'lstat', 'medv']

# Fit the scaler on the data and transform the specified columns
data[columns_to_scale] = scaler.fit_transform(data[columns_to_scale])

# Save the updated DataFrame back to the same CSV file (overwrite the original file)
data.to_csv(filepath, index=False)

# Confirm the changes were saved
print(data.head())
