# 7.2 Write a program that prompts for a file name, then opens that file 
# and reads through the file, looking for lines of the form:
#          X-DSPAM-Confidence:    0.8475
# Count these lines and extract the floating point values from each of the 
# lines and compute the average of those values and produce an output as shown below. 
# Do not use the sum() function or a variable named sum in your solution.
# You can download the sample data at http://www.py4e.com/code3/mbox-short.txt 
# when you are testing below enter mbox-short.txt as the file name.

# Prompting the user for a file name
file_name = input("Enter the file name: ")

try:
    # Opening the file
    with open(file_name, 'r') as file:
        # Initializing variables for counting and summing
        count = 0
        total_confidence = 0.0

        # Iterating through each line in the file
        for line in file:
            # Checking if the line starts with 'X-DSPAM-Confidence:'
            if line.startswith('X-DSPAM-Confidence:'):
                # Extracting the floating-point value from the line
                confidence_value = float(line.split(':')[-1].strip())
                
                # Counting and summing the values
                count += 1
                total_confidence += confidence_value

        # Calculating the average
        if count > 0:
            average_confidence = total_confidence / count
            print(f"Average spam confidence: {average_confidence:}")
        else:
            print("No X-DSPAM-Confidence lines found in the file.")

except FileNotFoundError:
    print(f"File '{file_name}' not found. Please enter a valid file name.")
except Exception as e:
    print(f"An error occurred: {e}")
