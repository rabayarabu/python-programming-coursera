# 8.5 Open the file mbox-short.txt and read it line by line. When you find a line that starts with 'From ' like the following line:
#                            *  From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008    *
# You will parse the From line using split() and print out the second word in the line
# (i.e. the entire address of the person who sent the message). Then print out a count at the end.
# Hint: make sure not to include the lines that start with 'From:'. Also look at the last line 
# of the sample output to see how to print the count.

# Open the file mbox-short.txt and read it line by line
file_name = 'mbox-short.txt'  # Update the file name accordingly

try:
    with open(file_name, 'r') as file:
        # Initialize a count variable
        count = 0

        # Read the file line by line
        for line in file:
            # Check if the line starts with 'From ' and not 'From:'
            if line.startswith('From ') and not line.startswith('From:'):
                # Parse the From line using split() and print the second word
                words = line.split()
                print(words[1])
                count += 1

        # Print the count at the end
        print(f"Total lines starting with 'From ': {count}")

except FileNotFoundError:
    print(f"File '{file_name}' not found. Please enter a valid file name.")
except Exception as e:
    print(f"An error occurred: {e}")
