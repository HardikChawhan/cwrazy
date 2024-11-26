# Step 1: Import the pandas library
import pandas as pd

# Step 2: Create a DataFrame from a dictionary of lists
data_dict = {
    "Name": ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank"],
    "Age": [25, 30, 35, 28, 22, 40],
    "Score": [85, 90, 88, 95, 80, 92]
}

# Convert dictionary to DataFrame
df = pd.DataFrame(data_dict)

# Step 3: Display the first few rows of the DataFrame
print("First Few Rows of the DataFrame:")
print(df.head())

# Step 4: Display the last few rows of the DataFrame
print("\nLast Few Rows of the DataFrame:")
print(df.tail())

# Step 5: Display information about the DataFrame
print("\nDataFrame Information:")
print(df.info())

# Step 6: Display basic statistics of the DataFrame
print("\nBasic Statistics of the DataFrame:")
print(df.describe())
