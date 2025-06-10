#Show a basic example of how to use matplotlib to plot a simple graph.
import matplotlib.pyplot as plt

def plot_simple_graph():
    # Sample data
    x = [1, 2, 3, 4, 5]
    y = [2, 3, 5, 7, 11]

    '''
    # Create a line plot
    plt.plot(x, y, marker='o')

    # Add labels and title
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Simple Line Plot')
    '''
    
    # Create a pie chart
    plt.pie(y, labels=x, autopct='%1.1f%%', startangle=140)
    # Add a title
    plt.title('Simple Pie Chart')
    # Set equal aspect ratio to ensure the pie chart is circular
    plt.axis('equal')
    
    # Show the plot
    plt.show()

# Example usage
if __name__ == "__main__":
    plot_simple_graph()