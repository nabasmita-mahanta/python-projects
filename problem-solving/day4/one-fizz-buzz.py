# Print the numbers from 1 to 100 that are divisible by 5
for num in range(1, 101):
    if num % 5 == 0:
        print(num)

# Print the numbers from 1 to 100 that are divisible by 3
for num in range(1, 101):
    if num % 3 == 0:
        print(num)

# Print the numbers from 1 to 100 that are divisible by both 5 and 3
# example - 15 is divisible by both 5 and 3
for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(num)

# Print the numbers from 1 to 100 that are divisible by 3 but not divisible by 6
# example - 3, 9, 15, 21 are divisible by 3 but not divisible by 6
for num in range(1, 101):
    if num % 3 == 0 and num % 6 != 0:
        print(num)

# Solve the fizz buzz problem in Hackerrank
# https://www.hackerrank.com/challenges/fizzbuzz/problem
"""
Write a short program that prints each number from 1 to 100 on a new line. 

For each multiple of 3, print "Fizz" instead of the number. 

For each multiple of 5, print "Buzz" instead of the number. 

For numbers which are multiples of both 3 and 5, print "FizzBuzz" instead of the number.
"""

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print("FizzBuzz")
    elif num % 3 == 0:
        print("Fizz")
    elif num % 5 == 0:
        print("Buzz")
    else:
        print(num)
