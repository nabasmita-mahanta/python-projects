# import prime-number.py
from utility import is_prime


# Write a python program to print all Prime Numbers from 0 to 1000
def print_prime_numbers_upto(number):
    for num in range(2, number + 1):
        if is_prime(num):
            print(num)


print_prime_numbers_upto(10000)

# def number():
#     for num in range(1, 10):
#         print(num)


# Write a python program to print the Nth Prime Number
N = int(input("To Print the Nth Prime No. Type N: "))
number_in_check = 2
counter = 0

while True:
    if is_prime(number_in_check):
        counter = counter + 1
        # print(f'{number_in_check} is the {counter}th prime number')
    else:
        # print(f'{number_in_check} is NOT prime number')
        pass

    if counter == N:
        break

    number_in_check = number_in_check + 1

print(f'{number_in_check} is the {counter}th prime number')
