# Write a python program to print the fibonacci sequence.

a = 0
b = 1
num = int(input("Enter a number to obtain fibonacci sequence: "))

if num ==1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(1,num+1):
        c = a + b
        a = b
        b = c
        print(c)



