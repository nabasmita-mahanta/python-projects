# Display Calendar in python.
import calendar
year = int(input("Enter year: "))
month = int(input("Enter month: "))

calendar = calendar.month(year,month)
print(calendar)

