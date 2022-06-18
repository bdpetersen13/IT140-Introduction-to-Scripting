"""
Print the two-dimensional list mult_table by row and column. Hint: Use nested loops.

Sample output with input: '1 2 3,2 4 6,3 6 9':
1 | 2 | 3
2 | 4 | 6
3 | 6 | 9
"""

user_input= input()
lines = user_input.split(',')

# This line uses a construct called a list comprehension, introduced elsewhere,
# to convert the input string into a two-dimensional list.
# Ex: 1 2, 2 4 is converted to [ [1, 2], [2, 4] ]

mult_table = [[int(num) for num in line.split()] for line in lines]

for row in mult_table:
    i = 0
    for num in row:
        if i < len(row)-1:
            print(row[i], end = ' | ')
            i = i + 1
        else:
            print(row[i])
