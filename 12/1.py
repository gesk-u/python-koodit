import requests
import json

request = "https://api.chucknorris.io/jokes/random"
response = requests.get(request)
data = response.json()
data = data["value"]

print(data)