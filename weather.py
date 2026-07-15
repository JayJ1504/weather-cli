# weather.py
import requests

def get_weather(city):
    api_key = "2ca1c32ecf9c6a8d237b91d94cd8cc80"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        return f"{data['name']}: {data['main']['temp']}°C, {data['weather'][0]['description']}"
    else:
        return "Error: City not found"
