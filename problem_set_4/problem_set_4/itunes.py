import json
import requests
import sys

# If the user does not provide two arguments, exit.
if len(sys.argv) != 2:
    sys.exit()

# Make an http using Python as the server.
response = requests.get('https://itunes.apple.com/search?entity=song&limit=50&term=' + sys.argv[1])
print(json.dumps(response.json(), indent = 2))

# Store the json response in a variable called o
o = response.json()
for result in o['results']:
    print(result['trackName'])