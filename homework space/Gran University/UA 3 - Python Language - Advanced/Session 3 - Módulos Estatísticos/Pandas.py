#Create a sample example to use the pandas library using a cities dataframe.
import pandas as pd

def show_cities_dataframe():
    # Create a sample DataFrame with city data
    data = {
        'City': ['New York', 'Los Angeles', 'Chicago', 'Houston', 'Phoenix'],
        'Population': [8419600, 3980400, 2716000, 2328000, 1690000],
        'Area (sq mi)': [302.6, 503.0, 227.3, 637.4, 517.6]
    }

    df = pd.DataFrame(data)

    # Display the DataFrame
    print("Cities DataFrame:")
    print(df)

    # Calculate and display the mean population
    mean_population = df['Population'].mean()
    print("\nMean Population:", mean_population)

    # Calculate and display the median area
    median_area = df['Area (sq mi)'].median()
    print("Median Area (sq mi):", median_area)
    # Calculate and display the standard deviation of population
    std_dev_population = df['Population'].std()
    print("Standard Deviation of Population:", std_dev_population)

# Call the function to show the results
show_cities_dataframe()
    