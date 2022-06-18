"""
Write an expression that executes the loop body as long as the user enters a non-negative number.

Note: If the submitted code has an infinite loop, the system will stop running the code after a few seconds and report "Program end never reached." The system doesn't print the test case that caused the reported message.

Sample outputs with inputs: 9 5 2 -1
Body
Body
Body
Done.
"""

user_num = int(input())
while user_num >= 0:
  print('Body')
  user_num = int(input())

print('Done.')
