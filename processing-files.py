# Prompting the user for a file name
file_name = input("Enter the file name: ")

try:
    # Opening the file
    with open(file_name, 'r') as file:
        # Reading the contents and printing in upper case after removing trailing whitespaces
        for line in file:
            print(line.rstrip().upper())

except FileNotFoundError:
    print(f"File '{file_name}' not found. Please enter a valid file name.")
except Exception as e:
    print(f"An error occurred: {e}")
