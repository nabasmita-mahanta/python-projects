# Program to find the sum of natural number.

num = int(input("Please enter a natural number:  "))
sum = 0

if num < 0:
    print("Please enter positive number")
else:
    for i in range(1, num + 1):
        sum = sum + i
    print(sum)
