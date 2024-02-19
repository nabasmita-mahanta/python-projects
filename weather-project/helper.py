import datetime


def generate_insert_query(result):
    latitude = result["coord"]["lat"]
    longitude = result["coord"]["lon"]

    weather_main = result["weather"][0]["main"]
    weather_description = result["weather"][0]["description"]

    temperature = int(result["main"]["temp"])
    temperature_feels_like = int(result["main"]["feels_like"])
    temperature_min = int(result["main"]["temp_min"])
    temperature_max = int(result["main"]["temp_max"])
    pressure = int(result["main"]["pressure"])
    humidity = int(result["main"]["humidity"])

    wind_speed = int(result["wind"]["speed"])

    date = result["dt"]
    print(date)
    print(type(date))
    dt_1 = 1708227182
    date_obj = datetime.datetime.fromtimestamp(date)
    print(date_obj)
    print(type(date_obj))

    country = result["sys"]["country"]

    sunrise = result["sys"]["sunrise"]
    sunrise_datetime_obj = datetime.datetime.fromtimestamp(sunrise)
    sunset = result["sys"]["sunset"]
    sunset_datetime_obj = datetime.datetime.fromtimestamp(sunset)

    timezone = result["timezone"]
    city_name = result["name"]

    query = (
        f"INSERT INTO weather_app.master_data (city_name, temp, temp_feels_like,weather_main,weather_desc,temp_min,temp_max,pressure, humidity, wind_speed, date, country, sunrise, sunset) "
        f"VALUES('{city_name}',{temperature},{temperature_feels_like},'{weather_main}','{weather_description}',{temperature_min},{temperature_max},{pressure},{humidity},{wind_speed},'{date_obj}','{country}','{sunrise_datetime_obj}','{sunset_datetime_obj}');")
    return query
