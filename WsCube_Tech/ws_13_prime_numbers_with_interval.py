# Write a python program to print all prime numbers in an interval.

for num in range(1, 50):
    if num == 1:
        pass
    elif num > 1:
        for i in range(2, num):
            if num% i == 0:
                break
        else:
            print(num)


