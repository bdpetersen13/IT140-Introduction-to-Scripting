"""
Type two statements. The first reads user input into person_name. The second reads user input into person_age. Use the int() function to convert person_age into an integer. Below is a sample output for the given program if the user's input is: Amy 4
In 5 years Amy will be 9
Note: Do not write a prompt for the input values.
"""

person_name = ''
person_age = 0

person_name = input()
person_age =  int(input())

print('In 5 years', person_name, 'will be', person_age + 5)
