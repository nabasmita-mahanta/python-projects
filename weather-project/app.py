import requests
import helper
import mysql.connector as sql
import config

prop = config.PROPERTIES
print(prop.get('cities'))

cities = prop.get('cities')
api_key = prop.get('api_openweathermap_key')

for city in cities:
    print(f"Checking weather data for {city}")

    # Get the weather data from openweathermap.org
    weather_data = requests.get(
        f"https://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&APPID={api_key}")

    # convert api result into Json
    result = weather_data.json()
    print(result)

    # Parse the api result into an insert query
    insert_query = helper.generate_insert_query(result)
    print(f"The insert query for {city} is {insert_query}")
    print("Making MySql connection")

    # Making MySql Connection
    connection = sql.connect(
        host=prop.get('api_openweathermap_key'),
        user=prop.get('database_mysql_username'),
        passwd=prop.get('database_mysql_password')
    )
    print("MySql Connection established")

    # Get the DB Cursor
    my_cursor = connection.cursor()
    my_cursor.execute(insert_query)
    print(f"Data for {city} inserted successfully")

    # Commit the DB Changes
    connection.commit()
