"""
Write a statement to add the key Tesla with value USA to car_makers. Modify the car maker of Fiat to Italy. Sample output for the given program:
Acura made in Japan
Fiat made in Italy
Tesla made in USA
"""

car_makers = {'Acura': 'Japan', 'Fiat': 'Egypt'}

# Add the key Tesla with value USA to car_makers
# Modify the car maker of Fiat to Italy
car_makers['Fiat'] = 'Italy'
car_makers['Tesla'] = 'USA'

print('Acura made in', car_makers['Acura'])
print('Fiat made in', car_makers['Fiat'])
print('Tesla made in', car_makers['Tesla'])
