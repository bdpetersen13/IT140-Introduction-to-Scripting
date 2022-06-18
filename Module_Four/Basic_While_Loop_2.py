"""
Write a while loop that prints user_num divided by 2 until user_num is less than 1. The value of user_num changes inside of the loop.

Sample output with input: 20
10.0
5.0
2.5
1.25
0.625


Note: If the submitted code has an infinite loop, the system will stop running the code after a few seconds and report "Program end never reached." The system doesn't print the test case that caused the reported message.
"""

user_num = int(input())

while user_num >= 1:
    user_num = user_num / 2
    print(user_num)
