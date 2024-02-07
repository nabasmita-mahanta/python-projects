import mysql.connector as sql

connection = sql.connect(host="localhost", user="root", passwd="admin123")
print(connection)
my_cursor = connection.cursor()
my_cursor.execute("show databases")

for result in my_cursor:
    print(result)
