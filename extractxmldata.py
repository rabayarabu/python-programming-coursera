import urllib.request
import xml.etree.ElementTree as ET

# Prompt for the URL
url = input('Enter location: ')

# Read the XML data from the URL
try:
    data = urllib.request.urlopen(url).read()
    print(f"Retrieving {url}")
    print(f"Retrieved {len(data)} characters")
except:
    print("Error retrieving data from the provided URL. Please check the URL and try again.")
    quit()

# Parse the XML data
tree = ET.fromstring(data)

# Find all 'count' elements using XPath
counts = tree.findall('.//count')

# Extract and sum the numbers
sum_counts = sum(int(count.text) for count in counts)

# Print the count and sum
print("Count:", len(counts))
print("Sum:", sum_counts)
