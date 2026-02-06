from dotenv import load_dotenv
import requests
import json
import os


load_dotenv()
WEATHER_API_KEY=os.getenv("OPENWEATHER_API_KEY")

#Stuttgart Coordinates
url = f"https://api.openweathermap.org/data/2.5/weather?lat=48.78&lon=9.17&appid={WEATHER_API_KEY}"

response = requests.get(url)
print(response)

if response.status_code != 200:
    print ("error:" "City not found")

data = response.json()
json_string = json.dumps(data, indent=4)
print(json_string)