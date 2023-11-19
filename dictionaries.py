# Initialize an empty dictionary to store sender counts
sender_counts = {}
# Open and read the "mbox-short.txt" file
with open('mbox-short.txt', 'r') as file:
    # Iterate through each line in the file
    for line in file:
        # Check if the line is starts with 'From '
        if line.startswith('From '):
            # Split the lines into words and get the sender(second)
            sender = line.split()[1]
            # Update the sender's count in the dictionary
            sender_counts[sender] = sender_counts.get(sender, 0) + 1
# Initialize variables to track the most prolific committer
max_sender = None
max_count = 0

# Find the most prolific committer using a maximum loop
for sender, count in sender_counts.items():
    if count > max_count:
        max_sender = sender
        max_count = count

# Print the result
print(f"The most prolific committer is '{max_sender}' with {max_count} messages.") 
