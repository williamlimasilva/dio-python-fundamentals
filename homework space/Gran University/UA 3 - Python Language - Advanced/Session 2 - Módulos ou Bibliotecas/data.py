#Create a example to show how to use the datetime library
import datetime
def show_datetime():
    # Get the current date and time
    now = datetime.datetime.now()
    
    # Format the date and time
    formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # Print the current date and time
    print("Current date and time:", formatted_date) 
# Example usage
if __name__ == "__main__":
    show_datetime()

