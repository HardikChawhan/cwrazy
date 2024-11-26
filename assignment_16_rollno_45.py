# Step 1: Import pandas library
import pandas as pd

# Step 2: Create a DataFrame with some sample data
data = {
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva", "Frank"],
    "Age": [25, 30, 35, 40, 45, 50],
    "Salary": [50000, 60000, 70000, 80000, 90000, 100000]
}

# Step 3: Convert the dictionary to a DataFrame
df = pd.DataFrame(data)

# Step 4: Filter rows based on a condition using boolean indexing
# Let's filter out the rows where Age is greater than or equal to 35
filtered_df = df[df["Age"] >= 35]

# Step 5: Sort the filtered DataFrame by 'Salary' in descending order
sorted_filtered_df = filtered_df.sort_values(by="Salary", ascending=False)

# Display the result
print("Filtered and Sorted DataFrame:")
print(sorted_filtered_df)
