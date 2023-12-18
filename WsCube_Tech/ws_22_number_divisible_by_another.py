# Write a python program to find numbers divisible  by another number.

num1 = int(input("please enter a number: "))

for number in range(1, 101):
    if number % num1 == 0:
        print(number)

# solution 2: using  Lambda function and filter()
l = [39, 48, 26, 98, 33, 67, 87]

result = list(filter(lambda x: x % 13 == 0, l))
print("The numbers divisible by 13 is", result)
