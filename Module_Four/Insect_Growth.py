"""
Given positive integer num_insects, write a while loop that prints that number doubled up to, but without exceeding 100. Follow each number with a space.

Sample output with input: 8
8 16 32 64
"""

num_insects = int(input()) # Must be >= 1

while num_insects <= 100:
    print(num_insects, end=' ')
    num_insects = num_insects * 2
    
