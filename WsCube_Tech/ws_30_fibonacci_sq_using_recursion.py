# Write a python program to display fibonacci sequence using recursion.
# recursion is a process in which a function calls itself directly or indirectly.
# here n represents number of terms.
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


n_terms = int(input("Enter a number here: "))
if n_terms <= 0:
    print("Enter a positive number")
else:
    print("Fibonacci Sequence")
    for i in range(n_terms):
        print(fibonacci(i))
