from fastapi import APIRouter
import requests
import os

router = APIRouter()

@router.get("/{city}")
async def get_weather(city: str):
    api_key = os.getenv("WEATHER_API_KEY")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    return response.json()
