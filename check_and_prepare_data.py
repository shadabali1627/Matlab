import pandas as pd
import numpy as np

# Read the data
data = pd.read_csv('sales_data.csv')

# Check for missing values
print(data.isnull().sum())

# Fill or drop missing values (depending on the context)
data.fillna(0, inplace=True)  # Example: Filling missing values with 0

# Ensure consistency (e.g., data types)
data['Date'] = pd.to_datetime(data['Date'])
data['Sales_Amount'] = data['Sales_Amount'].astype(float)
data['Quantity'] = data['Quantity'].astype(int)
