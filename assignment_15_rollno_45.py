# Step 1: Import pandas library
import pandas as pd

# Step 2: Create a DataFrame with some sample data
data = {
    "Category": ["A", "B", "A", "B", "A", "B", "A", "B"],
    "Value1": [10, 20, 30, 40, 50, 60, 70, 80],
    "Value2": [5, 15, 25, 35, 45, 55, 65, 75]
}

# Step 3: Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Step 4: Group the data by the 'Category' column
grouped = df.groupby("Category")

# Step 5: Calculate aggregate statistics on the grouped data
# Sum of each numeric column in each group
sum_data = grouped.sum()

# Mean of each numeric column in each group
mean_data = grouped.mean()

# Display the results
print("Sum of values by Category:")
print(sum_data)

print("\nMean of values by Category:")
print(mean_data)
