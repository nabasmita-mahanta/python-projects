# Write a python program to find armstrong in an interval.

lower = int(input("Please enter lower limit: "))
upper = int(input("Please enter upper limit: "))


def is_armstrong(number):
    length = len(number)
    sum = 0

    for i in number:
        sum = sum + (int(i) ** length)

    if sum == int(number):
        return True
    else:
        return False


for num in range(lower, upper + 1):
    if is_armstrong(str(num)):
        print(num)
