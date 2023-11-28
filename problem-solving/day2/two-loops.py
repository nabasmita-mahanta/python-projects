# Write a function that prints from 1 to 100 using for loop

def numbers():
    for number in range(1, 101):
        print(number)


numbers()


# Write a function that prints from 100 to 1 using for loop
def numbers():
    for number in reversed(range(1, 101)):
        print(number)


numbers()


# Write a function that prints from 1 to 100 and skipping 3 numbers in between
# eg - 1, 5, 9, 13 ... and so on

def new_numbers():
    for number in range(1, 101, 4):
        print(number)


new_numbers()


# Write a function that prints from 100 to 1 using while loop

def numbers(x):
    while x > 0:
        print(x)
        x = x - 1


numbers(100)


# Write a function that prints from 100 to 1 using do-while loop
# There is no do-while loop in python.


# Write a function that prints only EVEN numbers from 1 to 100

def even_numbers():
    for num in range(1, 101):
        if num % 2 == 0:
            print(num)


even_numbers()
