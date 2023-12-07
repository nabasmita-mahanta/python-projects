# Prime Number Program

"""
Given a positive integer N,
The task is to write a Python program to check if the number is Prime or not.
Print True if number is prime

Input:  n = 11
Output: True

Input:  n = 17
Output: True

Input:  n = 21
Output: False

Input:  n = 1
Output: False

Explanation: A prime number is a natural number greater than 1 that
has no positive divisors other than 1 and itself.
The first few prime numbers are {2, 3, 5, 7, 11, ….}.


A positive integer greater than 1
which has no other factors except 1 and the number itself is called a prime number.
2, 3, 5, 7 etc. are prime numbers as they do not have any other factors.
But 6 is not prime (it is composite) since, 2 x 3 = 6

Solution - https://www.programiz.com/python-programming/examples/prime-number
"""

number = int(input('Enter a positive number: '))


def is_prime(num):
    if num == 1:
        print("False")
    elif num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                print("False")
                break
        else:
            print("True")
    else:
        print("False")


is_prime(number)


