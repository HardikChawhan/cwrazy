# Step 1: Import the required library
import numpy as np

# Step 2: Create two NumPy arrays
array1 = np.array([10, 20, 30, 40])
array2 = np.array([1, 2, 3, 4])

# Step 3: Perform element-wise arithmetic operations
addition = np.add(array1, array2)       # Element-wise addition
subtraction = np.subtract(array1, array2)  # Element-wise subtraction
multiplication = np.multiply(array1, array2)  # Element-wise multiplication
division = np.divide(array1, array2)   # Element-wise division

# Step 4: Display the results of arithmetic operations
print("Array 1:", array1)
print("Array 2:", array2)
print("\nElement-wise Addition:", addition)
print("Element-wise Subtraction:", subtraction)
print("Element-wise Multiplication:", multiplication)
print("Element-wise Division:", division)

# Step 5: Use universal functions
sqrt_array1 = np.sqrt(array1)          # Square root of each element in array1
log_array1 = np.log(array1)            # Natural logarithm of each element in array1
exp_array1 = np.exp(array1)            # Exponential of each element in array1

# Step 6: Display the results of universal functions
print("\nSquare Root of Array 1:", sqrt_array1)
print("Natural Logarithm of Array 1:", log_array1)
print("Exponential of Array 1:", exp_array1)
