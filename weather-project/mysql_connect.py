import mysql.connector as sql

'''
@Author Nabasmita

This program creates database schema and tables
Run this program before running the main app
'''

# Create the connection
connection = sql.connect(host="localhost", user="root", passwd="Admin@123")
print(connection)

# Get the cursor
my_cursor = connection.cursor()

# Create Schema Query
create_schema = '''CREATE SCHEMA IF NOT EXISTS `weather_app` ;'''

# Create table query for master_data
create_table_master_data = ''' 
CREATE TABLE IF NOT EXISTS `weather_app`.`master_data` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `city_name` VARCHAR(45) NULL,
  `temp` INT NULL,
  `temp_feels_like` INT NULL,
  `weather_main` VARCHAR(45) NULL,
  `weather_desc` VARCHAR(450) NULL,
  `temp_min` INT NULL,
  `temp_max` INT NULL,
  `pressure` INT NULL,
  `humidity` INT NULL,
  `wind_speed` INT NULL,
  `date` DATETIME NULL,
  `country` VARCHAR(45) NULL,
  `sunrise` DATETIME NULL,
  `sunset` DATETIME NULL,
  PRIMARY KEY (`id`),
  UNIQUE INDEX `id_UNIQUE` (`id` ASC) VISIBLE);
'''

# Execute / Fire the queries

my_cursor.execute(create_schema)
print("\nCREATE SCHEMA Query Executed\nSchema created `weather_app`\n")

my_cursor.execute(create_table_master_data)
print("\nCREATE TABLE Query Executed\nTable Created `master_data`\n")

