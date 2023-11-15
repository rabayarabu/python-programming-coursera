# Open the file romeo.txt and read it line by line
file_name = 'romeo.txt'  # Update the file name accordingly

try:
    with open(file_name, 'r') as file:
        # Initialize an empty list to store unique words
        unique_words = []

        # Read the file line by line
        for line in file:
            # Split the line into a list of words
            words = line.split()

            # Iterate through each word in the line
            for word in words:
                # Check if the word is not already in the list and append it
                if word not in unique_words:
                    unique_words.append(word)

        # Sort and print the resulting words
        unique_words.sort()
        print(unique_words)

except FileNotFoundError:
    print(f"File '{file_name}' not found. Please enter a valid file name.")
except Exception as e:
    print(f"An error occurred: {e}")
