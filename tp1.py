<<<<<<< HEAD
import os
import requests

def get_weather(latitude, longitude):
    api_key = '442ed94cfe6ecc84c50d15ba360be7ce'
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

def main():
    latitude = float(os.environ.get('LATITUDE'))
    longitude = float(os.environ.get('LONGITUDE'))
    print(f"Latitude: {latitude} \nLongitude: {longitude}\n")
    weather_data = get_weather(latitude, longitude)
    
    if weather_data:
        print("Weather Information:")
        print(f"Description: {weather_data['description']}")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Wind Speed: {weather_data['wind_speed']} m/s")
    else:
        print("Failed to fetch weather data.")

if __name__ == "__main__":
    main()
=======
import os
import requests

def get_weather(latitude, longitude):
    api_key = '442ed94cfe6ecc84c50d15ba360be7ce'
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

def main():
    latitude = float(os.environ.get('LATITUDE'))
    longitude = float(os.environ.get('LONGITUDE'))
    print(f"Latitude: {latitude} \nLongitude: {longitude}\n")
    weather_data = get_weather(latitude, longitude)
    
    if weather_data:
        print("Weather Information:")
        print(f"Description: {weather_data['description']}")
        print(f"Temperature: {weather_data['temperature']}°C")
        print(f"Humidity: {weather_data['humidity']}%")
        print(f"Wind Speed: {weather_data['wind_speed']} m/s")
    else:
        print("Failed to fetch weather data.")

if __name__ == "__main__":
    main()
>>>>>>> 7ca80ccd536fc70700d1b028b7c4222ec40deba5
