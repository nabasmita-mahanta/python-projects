# Write a python program to swap two variable
# Solution 1
x = 13
y = 12
temp = x

x = y
y = temp

print("The value of x is ", x)
print("The value of y is", y)

# Solution 2
x = 13
y = 12
x, y = y, x
print("The value of x is ", x)
print("The value of y is", y)
