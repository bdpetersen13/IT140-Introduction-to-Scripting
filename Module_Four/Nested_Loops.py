"""
Given the number of rows and the number of columns, write nested loops to print a rectangle.

Sample output with inputs: 2 3
* * *
* * *
"""

num_rows = int(input())
num_cols = int(input())

for i in range(num_rows):
    print('*', end=' ')
    for j in range(num_cols - 1):
        i *= j

        print('*', end=' ')
    print()
