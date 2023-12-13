# Write a python program to check if the number is prime or not.

num = int(input("Please enter a number: "))

if num == 1:
    print("One is not a prime number")
elif num > 1:
    for i in range(2, num):
        if num % i == 0:
            print(num, " is not a prime number")
            break
    else:
        print(num, "is a prime number")
