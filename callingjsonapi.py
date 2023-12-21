import urllib.parse
import urllib.request
import json

def get_place_id(location):
    try:
        # Encode the location for the URL
        params = {'address': location, 'key': '42'}  # Replace 'your_api_key' with your actual API key
        url = 'http://py4e-data.dr-chuck.net/json?' + urllib.parse.urlencode(params)

        # Retrieve JSON data from the API
        print("Retrieving", url)
        with urllib.request.urlopen(url) as response:
            data = response.read().decode('utf-8')

        # Parse JSON data
        json_data = json.loads(data)

        # Extract and display the place_id
        place_id = json_data['results'][0]['place_id']
        print("Place id", place_id)

    except Exception as e:
        print("Error:", e)

# Prompt the user for a location
location = input("Enter location: ")

# Call the function with the provided location
get_place_id(location)
