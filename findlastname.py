import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

def retrieve_name(url, position, repetitions):
    for _ in range(repetitions):
        print("Retrieving:", url)
        html = urllib.request.urlopen(url).read()
        soup = BeautifulSoup(html, 'html.parser')

        # Retrieve all of the anchor tags
        tags = soup('a')
        target_tag = tags[position - 1] if len(tags) >= position else None

        if not target_tag:
            print(f"Position {position} not found on {url}")
            break

        url = target_tag.get('href', None)
        last_name = target_tag.contents[0]

    return last_name

# Example usage:
start_url = input('Enter URL: ')
repetitions = int(input('Enter count: '))
position = int(input('Enter position: '))

result_last_name = retrieve_name(start_url, position, repetitions)
print(f"The answer to the assignment for this execution is {result_last_name}.")
