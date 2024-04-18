from flask import Flask, jsonify, request
import os
import requests

app = Flask(__name__)

def get_weather(latitude, longitude):
    api_key = os.environ.get('API_KEY')
    url = f'http://api.openweathermap.org/data/2.5/weather?lat={latitude}&lon={longitude}&appid={api_key}'

    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        weather_info = {
            "description": data['weather'][0]['description'],
            "temperature": data['main']['temp'],
            "humidity": data['main']['humidity'],
            "wind_speed": data['wind']['speed']
        }
        return weather_info
    else:
        return "Error: Failed to retrieve weather data"
    
@app.route('/')
def weather_api():
    latitude = request.args.get('lat')
    longitude = request.args.get('lon')
    if latitude and longitude:
        weather_info = get_weather(latitude, longitude)
        return jsonify(weather=weather)
    else:
        return jsonify(error="Please provide latitude and longitude parameters"), 400


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)
