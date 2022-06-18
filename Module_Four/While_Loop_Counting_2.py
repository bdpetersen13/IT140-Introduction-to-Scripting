"""
Retype and run, note incorrect behavior. Then fix errors in the code, which should print num_stars asterisks.
while num_printed != num_stars:
    print('*')
Sample output with input: 3
*
*
*
"""

num_printed = 0

num_stars = int(input())

while num_printed < num_stars:
    print('*')
    num_printed += 1
