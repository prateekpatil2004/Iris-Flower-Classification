# 📁 src/load_from_csv.py

import pandas as pd

# Load the CSV file manually downloaded
df = pd.read_csv("data/IRIS.csv")

# Display the first few rows of the dataframe
print("First 5 records:")
print(df.head())
