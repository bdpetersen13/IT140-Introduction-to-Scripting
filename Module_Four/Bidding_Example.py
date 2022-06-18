"""
Write an expression that continues to bid until the user enters 'n'.

Sample output with inputs: 'y' 'y' 'n'
I'll bid $7!
Continue bidding? I'll bid $15!
Continue bidding? I'll bid $23!
Continue bidding?
"""

import random
random.seed(5)

keep_going = '-'
next_bid = 0

while keep_going != 'n':
   next_bid = next_bid + random.randint(1, 10)
   print('I\'ll bid ${}!'.format(next_bid))
   print('Continue bidding?', end=' ')
   keep_going = input()
