# Step 1: Import the required library
import numpy as np

# Step 2: Create a 1D NumPy array
array = np.arange(1, 13)  # Array with elements from 1 to 12
print("Original 1D Array:")
print(array)

# Step 3: Reshape the array into a 2D array (3x4)
reshaped_array = array.reshape(3, 4)
print("\nReshaped into 2D (3x4) Array:")
print(reshaped_array)

# Step 4: Transpose the reshaped array
transposed_array = reshaped_array.T
print("\nTranspose of the 2D Array:")
print(transposed_array)

# Step 5: Reshape the array into a 3D array (2x3x2)
reshaped_3d_array = array.reshape(2, 3, 2)
print("\nReshaped into 3D (2x3x2) Array:")
print(reshaped_3d_array)

# Step 6: Swap axes of the 3D array
swapped_axes_array = reshaped_3d_array.swapaxes(0, 1)  # Swap the first and second axes
print("\n3D Array after Swapping Axes (0 and 1):")
print(swapped_axes_array)
