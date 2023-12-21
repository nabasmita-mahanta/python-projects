# Write a python program to check whether a string is palindrome or not.

# Solution1:

word = input("Please enter a word here: ")


def palindrome(string):
    if word[:] == word[::-1]:
        print("Yes")
    else:
        print("No")


palindrome(word)

# solution 2




