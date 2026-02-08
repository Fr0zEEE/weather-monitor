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
def get_weather(city: str):
    WEATHER_API_KEY=os.getenv("OPENWEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={WEATHER_API_KEY}"
    response = requests.get(url)

    if response.status_code == 200:

        data = response.json()
        temp = data['main']['temp']
        desc = data['weather'][0]['description']
        city = data['name']
        hum = data['main']['humidity']
        wind_speed = data["wind"]["speed"]
        icon = data["weather"][0]["icon"]
        icon_url = f"http://openweathermap.org/img/wn/{icon}.png"

        weather_info = {"city": city,
                        "temperature": temp,
                        "description": desc,
                        "humidity": hum,
                        "windspeed": wind_speed,
                        "icon_url": icon_url}
        return weather_info

    elif response.status_code == 400:
        return{
                "error": "Bad Request",
                "status_code": 400}
    
    elif response.status_code == 401:
        return {
                "error": "Unauthorized",
                "status_code": 401}
    
    elif response.status_code == 404:
        return {                
                "error": "Not Found",
                "status_code": 404}
    
    elif response.status_code == 429:
        return {
                "error": "Too Many Requests",
                "status_code": 429}
    
    else:
        return {"message": "Something Went Wrong", 
                "status_code": response.status_code}