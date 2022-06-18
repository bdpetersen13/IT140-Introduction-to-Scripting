"""
Write a while loop that prints from 1 to user_num, increasing by 1 each time.

Sample output with input: 4
1
2
3
4
"""

i = 1

user_num = int(input()) # Assume positive

while i <= user_num:
    print(i)
    i = i +1 
