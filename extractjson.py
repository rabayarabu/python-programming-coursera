import urllib.request
import json

def get_comment_sum(url):
    try:
        # Retrieve JSON data from the URL
        print("Retrieving", url)
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')

        # Parse JSON data
        json_data = json.loads(data)

        # Extract comment counts and calculate the sum
        comments = json_data['comments']
        count_sum = sum(comment['count'] for comment in comments)

        # Display count and sum
        print("Count:", len(comments))
        print("Sum:", count_sum)

    except Exception as e:
        print("Error:", e)

# Prompt the user for a URL
url = input("Enter location: ")

# Call the function with the provided URL
get_comment_sum(url)
