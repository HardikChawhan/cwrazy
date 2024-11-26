# Step 1: Import the required library
try:
    import numpy as np
except ImportError:
    print("NumPy is not installed. Installing now...")
    import os
    os.system("pip install numpy")
    import numpy as np

# Step 2: Creating arrays using lists
list_array = np.array([1, 2, 3, 4, 5])


# Step 3: Creating arrays using built-in NumPy functions
zeros_array = np.zeros((2, 3))  # 2x3 array of zeros
ones_array = np.ones((3, 2))   # 3x2 array of ones
range_array = np.arange(0, 10, 2)  # Array with values from 0 to 9 with a step of 2

# Step 4: Displaying arrays and their attributes
print("Array created from list:")
print(list_array)
print("Shape:", list_array.shape, "Data type:", list_array.dtype, "Dimensions:", list_array.ndim)

print("\nArray of zeros:")
print(zeros_array)
print("Shape:", zeros_array.shape, "Data type:", zeros_array.dtype, "Dimensions:", zeros_array.ndim)

print("\nArray of ones:")
print(ones_array)
print("Shape:", ones_array.shape, "Data type:", ones_array.dtype, "Dimensions:", ones_array.ndim)

print("\nArray created with arange:")
print(range_array)
print("Shape:", range_array.shape, "Data type:", range_array.dtype, "Dimensions:", range_array.ndim)
