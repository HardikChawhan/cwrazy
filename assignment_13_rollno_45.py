# Step 1: Import the pandas library
import pandas as pd

# Step 2: Read data from a CSV file into a DataFrame
# Ensure the file 'data.csv' exists in the working directory
data = pd.read_csv('data.csv')

# Step 3: Display the first few rows of the DataFrame
print("First Few Rows of the DataFrame:")
print(data.head())

# Step 4: Display information about the DataFrame
print("\nDataFrame Information:")
print(data.info())

# Step 5: Display basic statistics of the DataFrame
print("\nBasic Statistics of the DataFrame:")
print(data.describe())

# Step 6: Save the DataFrame to a new CSV file after modifying (if needed)
# Example modification: Add a new column
data['NewColumn'] = 'Example'
data.to_csv('modified_data.csv', index=False)

print("\nModified DataFrame saved to 'modified_data.csv'.")
