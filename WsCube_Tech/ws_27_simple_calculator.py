# Write a python program to make a simple calculator.

# we will be making a simple calculator in
# which we can perform basic arithmetic operations
# like addition, subtraction, multiplication

print("~~~Mini Calculator~~~")

num1 = float(input("Please enter first number here: "))
num2 = float(input("Please enter second number here: "))

print("Press 1 for addition \nPress 2 for subtraction \nPress 3 for multiplication \nPress 4 for division")
choice = int(input("Please enter your preferred choice from 1-4: "))

if choice == 1:
    print("The addition of two number is: ", num1 + num2)
elif choice == 2:
    print("The subtraction of two number is: ", num1 - num2)
elif choice == 3:
    print("The multiplication of two number is: ", num1 * num2)
elif choice == 4:
    print("The division of two number is: ", num1 / num2)
else:
    print("Invalid Input")
