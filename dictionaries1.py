# Initialize an empty dictionary to store the counts for each hour
hour_counts = {}

# Open and read the mbox-short.txt file
with open('mbox-short.txt', 'r') as file:
    # Iterate through each line in the file
    for line in file:
        # Check if the line starts with 'From '
        if line.startswith('From '):
            # Split the line into words
            words = line.split()
            # Extract the time and split it to get the hour
            time = words[5]
            hour = time.split(':')[0]
            # Update the hour's count in the dictionary
            hour_counts[hour] = hour_counts.get(hour, 0) + 1

# Sort the dictionary by hour and print the counts
for hour, count in sorted(hour_counts.items()):
    print(f'{hour} {count}')