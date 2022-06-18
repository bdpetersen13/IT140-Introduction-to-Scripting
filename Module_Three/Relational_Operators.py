"""
Write an expression that will print "Dollar or more" if the value of num_cents is at least a dollar (100 cents is a dollar).

Sample output with input: 109
Dollar or more
"""

num_cents = int(input())
if num_cents >= 100:
    print('Dollar or more')
else:
    print('not a dollar')
