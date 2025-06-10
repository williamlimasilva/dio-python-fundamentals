#Create a example to show how to use the math library
import math
#External libraries are modules that provide additional functionality to Python.
import numpy as np
def show_math_operations():
    # Calculate the square root of 16
    sqrt_16 = math.sqrt(16)
    
    # Calculate the value of pi
    pi_value = math.pi
    
    # Calculate the sine of 90 degrees (converted to radians)
    sine_90 = math.sin(math.radians(90))
    
    # Print the results
    print("Square root of 16:", sqrt_16)
    print("Value of pi:", pi_value)
    print("Sine of 90 degrees:", sine_90)
# Example usage
if __name__ == "__main__":
    show_math_operations()

# Create a example to show how to use the numpy library
def show_numpy_operations():
    # Create a 1D array
    array_1d = np.array([1, 2, 3, 4, 5])
    
    # Calculate the mean of the array
    mean_value = np.mean(array_1d)
    
    # Create a 2D array (matrix)
    array_2d = np.array([[1, 2, 3], [4, 5, 6]])
    
    # Calculate the transpose of the 2D array
    transpose_array = np.transpose(array_2d)
    
    # Print the results
    print("1D Array:", array_1d)
    print("Mean of 1D Array:", mean_value)
    print("2D Array:\n", array_2d)
    print("Transpose of 2D Array:\n", transpose_array)
# Example usage
if __name__ == "__main__":
    show_numpy_operations()