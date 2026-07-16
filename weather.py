# weather.py
import requests

def get_weather(city):
    api_key = "2ca1c32ecf9c6a8d237b91d94cd8cc80"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            data = response.json()
            city_name = data['name']
            temp = data['main']['temp']
            humidity = data['main']['humidity']
            wind = data['wind']['speed']
            condition = data['weather'][0]['description']

            emoji_map = {
                "clear sky": "☀️",
                "few clouds": "🌤",
                "scattered clouds": "☁️",
                "broken clouds": "☁️",
                "shower rain": "🌧",
                "rain": "🌧",
                "thunderstorm": "⛈",
                "snow": "❄️",
                "mist": "🌫"
            }
            emoji = emoji_map.get(condition.lower(), "🌍")

            return (f"{emoji} {city_name}\n"
                    f"🌡 Temperature: {temp}°C\n"
                    f"💧 Humidity: {humidity}%\n"
                    f"💨 Wind Speed: {wind} m/s\n"
                    f"☁ Condition: {condition}")
        else:
            return "⚠️ City not found. Try again."
    except requests.exceptions.RequestException:
        return "⚠️ Network error. Please check your connection."