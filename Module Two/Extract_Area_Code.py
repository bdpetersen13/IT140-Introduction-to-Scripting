"""
Assign number_segments with phone_number split by the hyphens.

Sample output with input: '977-555-3221'
Area code: 977
"""

phone_number = input()
number_segments =  phone_number.split('-')
area_code = number_segments[0]
print('Area code:', area_code)
