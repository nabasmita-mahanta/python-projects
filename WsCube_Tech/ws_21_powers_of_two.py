# Write a python program to display powers of 2 using anonymous function.
# lamda function is the anonymous function here.


# using for loop only

# n_term = int(input("Please enter n th term: "))
#
# for i in range(1, n_term + 1):
#     result = 2 ** i
#     print(result)

# using anonymous function (lambda function)

n_terms = int(input("Please enter n th term: "))

result = list(map(lambda x: 2 ** x, range(n_terms + 1)))
# print(result)

for i in range(n_terms + 1):
    print("the value of 2 raised to power", i, "is", result[i])
