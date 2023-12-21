# Write a python program to remove punctuations from a string.
# punctuations are () {} - _ , "' = ! <>

punctuations = """!()-[]{};:'"\,<>./?@#$%^&*_~"""

user_input = input("Please enter a sentence here: ")
empty_string = ""

for i in user_input:
    if i not in punctuations:
        empty_string += i

print(empty_string)
