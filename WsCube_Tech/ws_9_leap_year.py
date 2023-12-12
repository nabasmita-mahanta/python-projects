# Write a python program to check if the number is leap year or not

year = int(input("Please enter a year: "))
if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a leap year")
