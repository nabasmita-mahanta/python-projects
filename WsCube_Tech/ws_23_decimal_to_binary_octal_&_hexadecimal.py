# write a python program to convert decimal to binary, octal & hexadecimal.

# Note: Base of decimal number is 10.
# base of binary number is 2
# base of octal number is 6
# base of hexadecimal number is 16

decimal = int(input("Enter a number here: "))

print("The conversion of decimal number", decimal, " is: ")
print(bin(decimal), " in binary")
print(oct(decimal), " in octal")
print(hex(decimal), " in hexadecimal")
