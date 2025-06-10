#create a example of file handling
try:
    # Open a file in write mode
    with open("example.txt", "w") as file:
        file.write("Hello, this is a test file.\n")
        file.write("This is the second line.\n")
        file.write("And this is the third line.\n")

    # Open the same file in read mode
    with open("example.txt", "r") as file:
        content = file.read()
        print("File content:")
        print(content)
except FileNotFoundError:
    print("Error: File not found.")
except IOError:
    print("Error: An I/O error occurred.")    
except Exception as e:
    print(f"An unexpected error occurred: {e}")
else:
    print("File operations were successful.")
finally:
    print("File handling completed.")