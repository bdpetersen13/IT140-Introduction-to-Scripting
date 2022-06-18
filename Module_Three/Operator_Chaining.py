"""
Write an expression that will print "in high school" if the value of user_grade is between 9 and 12 (inclusive).

Sample output with input: 10
in high school
"""

user_grade = int(input())
if 9<= user_grade <=12 :
    print('in high school')
else:
    print('not in high school')
