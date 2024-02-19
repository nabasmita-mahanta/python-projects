import requests
import helper
import mysql.connector as sql

cities = ['Delhi', 'Bangalore', 'Mumbai', 'Kolkata', 'Chennai', 'Guwahati', 'Hyderabad', 'Pune', 'Jaipur']
api_key = '3f9539b62b62177d2d723e8b117b9f2e'

for city in cities:
    print(f"Checking weather data for {city}")
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}")

    result = weather_data.json()
    print(result)
    insert_query = helper.generate_insert_query(result)
    print(f"The insert query for {city} is {insert_query}")
    print("Making MySql connection")
    # Making MySql Connection
    connection = sql.connect(host="localhost", user="root", passwd="Admin@123")
    print("MySql Connection established")
    my_cursor = connection.cursor()
    my_cursor.execute(insert_query)
    print(f"Data for {city} inserted successfully")
    connection.commit()


