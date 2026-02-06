from fastapi import FastAPI
import os
from dotenv import load_dotenv
import requests
#import json
#import logging

app = FastAPI()

load_dotenv()
WEATHER_API_KEY=os.getenv("OPENWEATHER_API_KEY")

@app.get("/ping")
def ping():
    return {"message": "pong"}

@app.get("/")
def home():
    return {"message": "homepage"}

@app.get("/weather")
def get_weather():
    WEATHER_API_KEY=os.getenv("OPENWEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?lat=48.78&lon=9.17&units=metric&appid={WEATHER_API_KEY}"
    response = requests.get(url)

    if response.status_code != 200:
        return {"message": "City not found"}
    
    data = response.json()
    temp = data['main']['temp']
    desc = data['weather'][0]['description']
    city = data['name']
    hum = data['main']['humidity']
    weather_info = {"city": city, "temperature": temp, "description": desc, "humidity": hum}



    return data