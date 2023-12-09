import re

# Open the file
filename = 'regex_sum_1923930.txt'  # Replace with your file name
with open(filename, 'r') as file:
    # Read the content of the file
    content = file.read()

# Find all the numbers in the content using regular expression
numbers = re.findall('[0-9]+', content)

# Convert the extracted strings to integers and calculate the sum
total_sum = sum(map(int, numbers))

# Print the sum
print("Sum:", total_sum)
