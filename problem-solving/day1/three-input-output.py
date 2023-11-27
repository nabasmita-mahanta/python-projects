# Write a python program that asks the user for name and age
# After that write a function named "greetUser"
# that takes in the name and age and gender and prints a beautiful message
# like -> Hello Max, you are 30 years old


name = input("Please enter your name: ")
age = input("Please enter your age: ")


def greet_user(nm, ag):
    print("Hello " + nm + ", " + "you are " + ag + " years old")


greet_user(name, age)

# Write a python program that asks the user for name and age
# After that write a function named "is_eligible_to_vote"
# that takes in the name and age and gender and prints a message

# like -> Hello Max, you are 30 years old, and eligible to vote
# Hello Max, you are 14 years old, and NOT eligible to vote
# All people of 18 and above are eligible to vote

new_name = input("Please enter your name: ")
new_age = input("Please enter your age: ")


def is_eligible_to_vote(nm, ag):
    if int(new_age) >= int(18):
        print("Hello " + nm + ", " + "you are " + str(ag) + " years old, and eligible to vote")
    else:
        print("Hello " + nm + ", " + "you are " + str(ag) + " years old, and not eligible to vote")


is_eligible_to_vote(name, age)
