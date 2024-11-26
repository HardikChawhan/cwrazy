# Step 1: Import pandas library
import pandas as pd

# Step 2: Create a DataFrame with some sample data, including missing values (NaN)
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [25, None, 35, 40, None],
    "Salary": [50000, 60000, None, 80000, 90000],
    "Department": ["HR", "IT", "Finance", None, "Marketing"]
}

# Step 3: Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Step 4: Display the original DataFrame with missing values
print("Original DataFrame with missing values:")
print(df)

# Step 5: Handling missing values using fillna() (filling NaN values with a specified value)
df_filled = df.fillna({
    "Age": df["Age"].mean(),          # Fill missing Age with the mean of the Age column
    "Salary": df["Salary"].mean(),    # Fill missing Salary with the mean of the Salary column
    "Department": "Unknown"           # Fill missing Department with 'Unknown'
})

# Step 6: Handling missing values using dropna() (dropping rows with NaN values)
df_dropped = df.dropna()  # This will drop any rows with NaN values

# Step 7: Perform aggregation operations on the DataFrame
age_sum = df_filled["Age"].sum()  # Sum of Age column
salary_mean = df_filled["Salary"].mean()  # Mean of Salary column
age_mean = df_filled["Age"].mean()  # Mean of Age column
salary_sum = df_filled["Salary"].sum()  # Sum of Salary column

# Step 8: Display results
print("\nDataFrame after filling missing values (fillna()):")
print(df_filled)

print("\nDataFrame after dropping rows with missing values (dropna()):")
print(df_dropped)

print("\nAggregated Data (Sum and Mean):")
print(f"Sum of Age: {age_sum}")
print(f"Mean of Age: {age_mean}")
print(f"Mean of Salary: {salary_mean}")
print(f"Sum of Salary: {salary_sum}")
