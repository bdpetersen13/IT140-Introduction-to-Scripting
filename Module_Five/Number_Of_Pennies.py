"""
Write a function number_of_pennies() that returns the total number of pennies given a number of dollars and (optionally) a number of pennies.

Sample output with inputs: 5 6 4
506
400
"""

def number_of_pennies(dollars = 0, pennies = 0):
    return dollars * 100 + pennies

print(number_of_pennies(int(input()), int(input()))) # Both dollars and pennies
print(number_of_pennies(int(input())))               # Dollars only
