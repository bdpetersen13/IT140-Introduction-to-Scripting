"""
Many user-created passwords are simple and easy to guess. Write a program that takes a simple password and makes it stronger by replacing characters using the key below, and by appending "q*s" to the end of the input string.

i becomes !
a becomes @
m becomes M
B becomes 8
o becomes .
Ex: If the input is:

mypassword
the output is:

Myp@ssw.rdq*s
Hint: Python strings are immutable, but support string concatenation. Store and build the stronger password in the given password variable.
"""

word = input()
password = ''

for x in word:
    if x == 'i':
        password += '!'
    elif x == 'a':
        password += '@'
    elif x == 'm':
        password += 'M'
    elif x == 'B':
        password += '8'
    elif x == 'o':
        password += '.'
    else:
        password += x

password += 'q*s'

print(password)
