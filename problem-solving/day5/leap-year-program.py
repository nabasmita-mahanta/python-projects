# Leap Year Program

"""
A leap year program in Python takes a year as input
and checks if the year is a leap year or not.

A leap year is a year that follows any one of the below-specified conditions:
Year divisible by 400.
Year divisible by 4 but not by 100.

Input 1: 2000
Output 1: Yes

Input 2: 1877
Output 2: No

Write a program in python to check whether a given year is leap year or not
"""

year = int(input('Enter any year: '))


def is_leap_year(num):
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print('Yes')
    else:
        print('No')


is_leap_year(year)
