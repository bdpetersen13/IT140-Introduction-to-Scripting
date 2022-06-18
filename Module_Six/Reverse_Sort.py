"""
Sort short_names in reverse alphabetic order.

Sample output with input: 'Jan Sam Ann Joe Tod'
['Tod', 'Sam', 'Joe', 'Jan', 'Ann']
"""

user_input = input()
short_names = user_input.split()

short_names.sort()
short_names.reverse()

print(short_names)
