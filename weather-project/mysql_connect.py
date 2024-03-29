import mysql.connector as sql

connection = sql.connect(host="localhost", user="root", passwd="admin123")
print(connection)
my_cursor = connection.cursor()
create_schema = '''CREATE SCHEMA `weather_app` ;'''
create_table_query = ''' 
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
# my_cursor.execute(create_schema)
my_cursor.execute(create_table_query)

