# Write a python program to display the multiplication table.

num = int(input("Please enter the number for multiplication table: "))

for i in range(1, 11):
    result = num * i
    print(str(num) + " * " + str(i) + " =" + str(result))
