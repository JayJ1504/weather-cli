# Weather Runner 🌦🤖

A compact desktop weather app built with **Python (Tkinter)** and the **OpenWeather API** that blends practical weather data with a retro‑futuristic animated runner, dynamic day/night cycles, and seasonal visual effects.

---

## Demo
Add a short GIF or screenshot here showing the app running (place file `demo.gif` or `screenshot.png` in the repo and reference it).

---

## Features
- **Search** for weather by city.
- **Displays:** city name, temperature (°C), humidity, wind speed, and condition with emoji.
- **Animated runner:** looping transparent GIF of a retro robot runner.
- **Day/night cycle:** background color transitions through day, noon, sunset, and night.
- **Seasonal effects:** auto‑detects the system month and shows snow, rain, leaves, or clear sky.
- **Lightweight UI:** single-file GUI (`app.py`) and a small `weather.py` module for API calls.

---

## Tech Stack
- **Python 3**
- **Tkinter** for GUI
- **Requests** for HTTP calls to OpenWeather
- **OpenWeather API** for live weather data

---

## Installation and Run
1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/<repo-name>.git
   cd <repo-name>

Install dependencies: pip install requests
Ensure runner.gif is in the project root (or assets/runner.gif if you moved it).
Run the app---> python app.py

Files and Structure:
weather-runner/
├── app.py            # GUI, animation, seasonal effects
├── weather.py        # OpenWeather API wrapper
├── runner.gif        # Animated runner asset (transparent GIF)
├── README.md
└── .gitignore

Configuration
OpenWeather API Key  
The weather.py file currently contains an API key variable. Replace it with your own key if needed: api_key = "YOUR_API_KEY"
Asset Path  
If you move runner.gif into an assets/ folder, update the path in app.py: tk.PhotoImage(file="assets/runner.gif", format=f"gif -index {i}").

