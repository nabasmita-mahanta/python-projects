# Write a python program to check armstrong number.
# A armstrong number is one whose sum of digits raised to the power of the length of the number
# equals the number itself.
# 371, for example, is an Armstrong number because 3**3 + 7**3 + 1**3 = 371

num = input("Please enter a number: ")


# length = len(num)
# sum = 0
#
# for i in num:
#     sum = sum + (int(i) ** length)
# result = sum
# print(result)
#
# if result == int(num):
#     print("Armstrong number")
# else:
#     print("Not a armstrong number")

def is_armstrong(number):
    length = len(number)
    sum = 0

    for i in number:
        sum = sum + (int(i) ** length)

    if sum == int(number):
        return True
    else:
        return False


if is_armstrong(num):
    print("Armstrong")
else:
    print("Not armstrong")
