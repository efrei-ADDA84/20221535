import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)
api_key = get.env(api_key)

def get_weather(latitude, longitude, api_key):
    url = f"http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}&units=metric"
    print("Appel de l'API en cours...")
    response = requests.get(url)
    data = response.json()
    
    if response.status_code == 200:
        weather_info = {
            "description": data['weather'][0]['description'],
            "temperature": data['main']['temp'],
            "humidity": data['main']['humidity'],
            "wind_speed": data['wind']['speed']
        }
        return weather_info
    else:
        return None

@app.route('/')
def weather():
    latitude = float(os.environ.get('LATITUDE'))
    longitude = float(os.environ.get('LONGITUDE'))
    # api_key = os.environ.get('OPENWEATHER_API_KEY')
    api_key = "442ed94cfe6ecc84c50d15ba360be7ce"
    weather_data = get_weather(latitude, longitude, api_key)
    
    if weather_data:
        return jsonify(weather_data)
    else:
        return "Failed to fetch weather data.", 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
