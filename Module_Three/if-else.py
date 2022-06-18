"""
Write an expression that will cause the following code to print "18 or less" if the value of user_age is 18 or less. Write only the expression.

Sample output with input: 17
18 or less
"""

user_age = int(input())
if  user_age <= 18:
   print('18 or less')
else:
   print('Over 18')
