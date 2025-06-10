#Create examples showing how to calculate the mean, median, and standard deviation using the numpy library
import numpy as np

def show_numpy_statistics():
    # Create a sample array
    data = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    
    # Calculate mean
    mean = np.mean(data)
    print("Mean:", mean)
    
    # Calculate median
    median = np.median(data)
    print("Median:", median)
    
    # Calculate standard deviation
    std_dev = np.std(data)
    print("Standard Deviation:", std_dev)

# Example usage
if __name__ == "__main__":
    show_numpy_statistics()

# Create examples showing how to calculate the mean, median, and standard deviation no using the numpy library without using external libraries.
def show_statistics_without_numpy():
    # Create a sample data list
    data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    # Calculate mean
    mean = sum(data) / len(data)
    print("Mean:", mean)
    
    # Calculate median
    data.sort()
    if len(data) % 2 == 1:
        median = data[len(data) // 2]
    else:
        median = (data[len(data) // 2 - 1] + data[len(data) // 2]) / 2
    print("Median:", median)
    # Calculate standard deviation
    squared_diffs = [(x - mean) ** 2 for x in data]
    std_dev = (sum(squared_diffs) / len(data)) ** 0.5
    print("Standard Deviation:", std_dev)
# Example usage
if __name__ == "__main__":
    show_statistics_without_numpy()
