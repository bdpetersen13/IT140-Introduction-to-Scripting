"""
Write a program that gets a list of integers from input, and outputs non-negative integers in ascending order (lowest to highest).

Ex: If the input is:

10 -7 4 39 -6 12 2
the output is:

2 4 10 12 39
For coding simplicity, follow every output value by a space. Do not end with newline.
"""

user_input = input()

my_list = [int(i) for i in user_input.split() if (int(i)>=0)]

my_list.sort()

[print(i, end=' ') for i in my_list]
