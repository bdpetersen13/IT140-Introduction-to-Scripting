"""
Given num_rows and num_cols, print a list of all seats in a theater. Rows are numbered, columns lettered, as in 1A or 3E. Print a space after each seat.

Sample output with inputs: 2 3
1A 1B 1C 2A 2B 2C
"""

num_rows = int(input())
num_cols = int(input())

# Note 1: You will need to declare more variables
# Note 2: Place end=' ' at the end of your print statement to separate seats by spaces

rows = 1
for i in range(num_rows):
    cols = 'A'
    for j in range(num_cols):
        print(str(rows) + cols, end=' ')
        cols = chr(ord(cols) + 1)
    rows += 1
    
print()
