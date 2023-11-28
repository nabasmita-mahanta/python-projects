# Write a function 'is_even' that takes a number
# and returns True if number is even, and False otherwise

def is_even(x):
    if x % 2 == 0:
        return True
    else:
        return False


print(is_even(6))


# Write a function 'is_even' that takes two numbers
# and returns True if both numbers are even, and False otherwise

def is_even(x, y):
    if x % 2 == 0 and y % 2 == 0:
        return True
    else:
        return False


print(is_even(7, 8))


# Write a function 'is_even' that takes two numbers
# and returns True if any of the number is even, and False otherwise
def is_even(x, y):
    if x % 2 == 0 or y % 2 == 0:
        return True
    else:
        return False


print(is_even(6, 7))


# Write a function 'highest_num' that takes TWO numbers
# and returns the highest number
def highest_num(x, y):
    if x > y:
        return x
    else:
        return y


print(highest_num(4, 5))


# Write a function 'highest_num' that takes THREE numbers
# and returns the highest number
def highest_num(x, y, z):
    if x > y and x > z:
        return x
    elif y > x and y > z:
        return y
    else:
        return z


print(highest_num(2, 10, 7))
