import requests
import json

# Step 1: Get an access token
access_token = "e1f16f917b7245a1a75e52973ad2211c"

# Step 2: Search for an item
query = "Subtronics"
type = "event"
url = f"https://api.spotify.com/v1/search?q={query}&type={type}"
headers = {"Authorization": f"Bearer {access_token}"}
response = requests.get(url, headers=headers)

# Step 3: Parse the response
data = response.json()

# Step 4: Extract the relevant concert information
concerts = data["events"]

# Step 5: Write the concert information to a JSON file

# with open("subtronics_concerts.json", "w") as outfile:
#    json.dump(concerts, outfile)
print(concerts)
