# Step 1: Import the required library
import numpy as np

# Step 2: Create a sample NumPy array
data = np.array([15, 20, 35, 40, 50, 60, 75, 80, 95, 100])
print("Original Array:")
print(data)

# Step 3: Calculate basic statistical properties
mean_value = np.mean(data)
median_value = np.median(data)
std_deviation = np.std(data)
variance_value = np.var(data)

print("\nStatistical Properties:")
print(f"Mean: {mean_value}")
print(f"Median: {median_value}")
print(f"Standard Deviation: {std_deviation}")
print(f"Variance: {variance_value}")

# Step 4: Compute percentiles
percentiles = [25, 50, 75]  # Example percentiles
percentile_values = np.percentile(data, percentiles)

print("\nPercentile Values:")
for p, value in zip(percentiles, percentile_values):
    print(f"{p}th Percentile: {value}")

# Step 5: Compute correlation coefficient
# Creating another array to calculate correlation with
data2 = np.array([5, 15, 25, 35, 45, 55, 65, 75, 85, 95])

correlation_coefficient = np.corrcoef(data, data2)
print("\nCorrelation Coefficient Matrix:")
print(correlation_coefficient)
