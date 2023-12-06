# Write a function 'digits' that takes a number
# and prints digits of that number
# eg digits(6475)

# OUTPUT
# 6
# 4
# 7
# 5

# def digits():
#     number = input("Please enter some digits: ")
#     for digit in number:
#         print(digit)
#
#
# digits()

def digits(number):
    for dig in number:
        print(dig)


digits(str(7890))


# Write a function 'length_of_num' that takes a number
# and prints length that number
# eg length_of_num(64751)

# OUTPUT
# 5

def length_of_num(number):
    print(len(number))


length_of_num(str(6750))


# Write a function 'last_digit' that takes a number
# and returns the last digits of that number
# eg last_digit(647) -> print 7, the last digit

def last_digit(number):
    print(number[-1])


last_digit(str(647))


# Write a function 'sum_of_digits' that takes a number
# and returns the sum of the digits of that number
# eg sum_of_digits(647) -> 6+4+7 = 17 -> print 17

def sum_of_digits(number):
    sum = 0
    for num in number:
        sum = sum + int(num)
    return sum


print(sum_of_digits(str(987)))
