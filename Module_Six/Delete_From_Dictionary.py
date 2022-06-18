"""
Delete Prussia from country_capital.

Sample output with input: 'Spain:Madrid,Togo:Lome,Prussia: Konigsberg'
Prussia deleted? Yes.
Spain deleted? No.
Togo deleted? No.
"""

user_input = input()
entries = user_input.split(',')
country_capital = {}

for pair in entries:
    split_pair = pair.split(':')
    country_capital[split_pair[0]] = split_pair[1]
    # country_capital is a dictionary, Ex. { 'Germany': 'Berlin', 'France': 'Paris'

''' Your solution goes here '''

print('Prussia deleted?', end=' ')
if 'Prussia' in country_capital:
    print('No.')
else:
    print('Yes.')

print ('Spain deleted?', end=' ')
if 'Spain' in country_capital:
    print('No.')
else:
    print('Yes.')

print ('Togo deleted?', end=' ')
if 'Togo' in country_capital:
    print('No.')
else:
    print('Yes.')
