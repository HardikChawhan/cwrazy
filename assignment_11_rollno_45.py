# Step 1: Import the required library
import numpy as np

# Step 2: Create a sample 2D NumPy array
array = np.array([
    [10, 20, 30, 40],
    [50, 60, 70, 80],
    [90, 100, 110, 120]
])
print("Original Array:")
print(array)

# Step 3: Demonstrate basic indexing
print("\nAccessing specific elements:")
print("Element at (0, 2):", array[0, 2])  # Access element in the first row, third column
print("Element at (2, 1):", array[2, 1])  # Access element in the third row, second column

# Step 4: Demonstrate slicing
print("\nSlicing examples:")
print("First row:", array[0, :])  # First row
print("Second column:", array[:, 1])  # Second column
print("Subarray (first two rows, last two columns):")
print(array[:2, 2:])

# Step 5: Demonstrate Boolean indexing
print("\nBoolean Indexing:")
boolean_mask = array > 50
print("Boolean mask:\n", boolean_mask)
print("Elements greater than 50:", array[boolean_mask])

# Step 6: Demonstrate fancy indexing
print("\nFancy Indexing:")
rows = [0, 2]  # Select the first and third rows
columns = [1, 3]  # Select the second and fourth columns
print("Elements at positions (0,1) and (2,3):", array[rows, columns])
print("Rows selected using fancy indexing:")
print(array[rows, :])

# Step 7: Demonstrate multidimensional fancy indexing
print("\nMultidimensional Fancy Indexing:")
row_indices = np.array([0, 1, 2])
column_indices = np.array([3, 2, 1])
print("Elements at (0,3), (1,2), (2,1):", array[row_indices, column_indices])
