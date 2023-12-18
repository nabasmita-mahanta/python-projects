# Write a python program to find factor of a number.

num = int(input("enter a number: "))

for i in range(1, num + 1):
    if num % i == 0:
        print("The factor of ",num,"is ", i)
