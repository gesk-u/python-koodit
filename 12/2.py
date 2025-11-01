import requests

from dotenv import dotenv_values

config = dotenv_values(".env")
API_KEY = config['WEATHER']


BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

municipality = input("Name of a municipality: ")

params = {
    "q": municipality,
    "appid": API_KEY,
    "units": "metric",
}

try:
    response = requests.get(BASE_URL, params=params)
    response.raise_for_status()
    data = response.json()

    description = data["weather"][0]["description"]
    temperature = data["main"]["temp"]

    print(f"Weather in {municipality}: {description}")
    print(f"Temperature: {temperature:.1f}°C")
except requests.exceptions.HTTPError:
    print("Sorry, something went wrong...Check the name of the city")
except requests.exceptions.RequestException as e:
    print("Network error", e)