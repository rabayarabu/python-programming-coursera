import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# Get the URL from the user
url = input("Enter URL: ")

# Read the HTML from the URL
html = urllib.request.urlopen(url).read()

# Parse the HTML using BeautifulSoup
soup = BeautifulSoup(html, 'html.parser')

# Find all span tags
tags = soup('span')

# Initialize count and sum variables
count = 0
sum_numbers = 0

# Loop through the span tags
for tag in tags:
    # Extract the content of the span tag
    content = tag.contents[0]

    # Convert the content to an integer and add to the sum
    sum_numbers += int(content)

    # Increment the count
    count += 1

# Print the count and sum
print("Count", count)
print("Sum", sum_numbers)
