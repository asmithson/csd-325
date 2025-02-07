import requests
import json

# URL to the API
url = "https://www.dnd5eapi.co/api/spells/magic-missile/"

def jprint(obj):
    """Function to format and print JSON nicely"""
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# Make the request
response = requests.get(url)

# Print status code
print(f"Status Code: {response.status_code}")

# Print unformatted raw JSON response
print("\nRaw JSON Response:")
print(response.text)  # No formatting

# Print formatted JSON response
if response.status_code == 200:
    try:
        json_data = response.json()
        print("\nFormatted JSON Response:")
        jprint(json_data)
    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
