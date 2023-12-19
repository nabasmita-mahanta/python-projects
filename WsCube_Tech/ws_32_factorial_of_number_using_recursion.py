# python program to find factorial of number using recursion.

def factorial_of_number(n):
    if n <= 1:
        return n
    else:
        return n * factorial_of_number(n - 1)


n = int(input("Enter a number here: "))
if n <= 0:
    print("Factorial number less than 1 does not exist")
else:
    print("Factorial of given number is: ", factorial_of_number(n))
