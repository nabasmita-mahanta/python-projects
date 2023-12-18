# Write a python program to find HCF or GCD of two numbers.
# HCF = highest common factor GCD = Greatest common divisor

def find_HCF(x, y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1, smaller + 1):
        if x % i == 0 and y % i == 0:
            hcf = i
    return hcf


print("The HCF of the given two numbers is", find_HCF(20, 30))
