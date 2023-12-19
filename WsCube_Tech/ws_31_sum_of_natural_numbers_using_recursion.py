# Write a python program to display sum of natural numbers using recursion.

# sum = 0
# for num in range(1, 10):
#     sum = sum + num
# print(sum)

def sum_of_natural_no(n):
    if n <= 1:
        return n
    else:
        return n + sum_of_natural_no(n - 1)


n = int(input('Enter a number here: '))

if n <= 0:
    print("enter a positive number")
else:
    print("The sum of natural number upto given number is", sum_of_natural_no(n))
