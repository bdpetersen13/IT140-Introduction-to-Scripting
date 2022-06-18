"""
Write a program whose inputs are three integers, and whose output is the smallest of the three values.

Ex: If the input is:

7
15
3
the output is:

3
"""

user_input1 = int(input())
user_input2 = int(input())
user_input3 = int(input())

smallest_input = user_input1

if user_input2 < smallest_input:
    smallest_input = user_input2

if user_input3 < smallest_input:
    smallest_input = user_input3

print(smallest_input)
