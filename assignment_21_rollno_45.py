import numpy as np

# Step 1: Create a NumPy array
array = np.array([[1, 2, 3, 4],
                  [5, 6, 7, 8],
                  [9, 10, 11, 12],
                  [13, 14, 15, 16]])

print("Original Array:")
print(array)

# Step 2: Accessing specific elements (e.g., element at row 1, column 2)
# Access element at row 1, column 2
element = array[1, 2]  # Row 1, Column 2 (zero-indexed)
print("\nElement at row 1, column 2:", element)

# Step 3: Accessing specific rows (e.g., row 2)
# Access the second row
row_2 = array[1, :]
print("\nSecond row (row 1 in zero-indexing):")
print(row_2)

# Step 4: Accessing specific columns (e.g., column 3)
# Access the third column
col_3 = array[:, 2]
print("\nThird column:")
print(col_3)

# Step 5: Slicing operations
# Extract a subarray (first 2 rows, first 3 columns)
subarray = array[:2, :3]
print("\nSubarray (first 2 rows and first 3 columns):")
print(subarray)

# Extract a subarray (rows 2 to 3, columns 2 to 3)
subarray2 = array[1:3, 1:3]
print("\nSubarray (rows 2 to 3, columns 2 to 3):")
print(subarray2)

# Step 6: Boolean Indexing
# Create a boolean mask: True for elements greater than 10
mask = array > 10
print("\nBoolean Mask (elements > 10):")
print(mask)

# Use the boolean mask to extract elements greater than 10
filtered_elements = array[mask]
print("\nFiltered elements (greater than 10):")
print(filtered_elements)

# Step 7: Fancy Indexing
# Fancy indexing allows selecting multiple rows/columns by passing a list of indices
rows = [0, 2]  # Select the first and third rows
cols = [1, 3]  # Select the second and fourth columns

fancy_indexed_array = array[rows, cols]
print("\nFancy Indexed Array (first and third rows, second and fourth columns):")
print(fancy_indexed_array)

# Select non-contiguous rows and columns using fancy indexing
fancy_indexed_rows = array[[0, 2], :]  # Select first and third rows
fancy_indexed_cols = array[:, [1, 3]]  # Select second and fourth columns

print("\nFancy Indexed Rows (first and third rows):")
print(fancy_indexed_rows)

print("\nFancy Indexed Columns (second and fourth columns):")
print(fancy_indexed_cols)
