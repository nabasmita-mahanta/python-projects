import requests

cities = ['Delhi', 'Bangalore', 'Mumbai', 'Kolkata', 'Chennai', 'Guwahati', 'Hyderabad', 'Pune', 'Jaipur']
api_key = '3f9539b62b62177d2d723e8b117b9f2e'

for city in cities:
    print(f"Checking weather data for {city}")
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}")

    print(weather_data.json())
    result = weather_data.json()
    print(type(result))
    print(result["coord"])

    latitude = result["coord"]["lat"]
    longitude = result["coord"]["lon"]

    weather_main = result["weather"][0]["main"]
    weather_description = result["weather"][0]["description"]

    temperature = result["main"]["temp"]
    temperature_feels_like = result["main"]["feels_like"]
    temperature_min = result["main"]["temp_min"]
    temperature_max = result["main"]["temp_max"]
    pressure = result["main"]["pressure"]
    humidity = result["main"]["humidity"]

    wind_speed = result["wind"]["speed"]

    date = result["dt"]

    country = result["sys"]["country"]
    sunrise = result["sys"]["sunrise"]
    sunset = result["sys"]["sunset"]

    timezone = result["timezone"]
    city_name = result["name"]
