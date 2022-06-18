"""
Write an expression using membership operators that prints "Special number" if special_num is one of the special numbers stored in the list special_list = [-99, 0, or 44].

Sample output with input: 17
Not special number
"""

special_list = [-99, 0, 44]
special_num = int(input())

if special_num in special_list:
    print('Special number')
else:
    print('Not special number')
