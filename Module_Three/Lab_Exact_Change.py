"""
Write a program with total change amount as an integer input, and output the change using the fewest coins, one coin type per line. The coin types are Dollars, Quarters, Dimes, Nickels, and Pennies. Use singular and plural coin names as appropriate, like 1 Penny vs. 2 Pennies.

Ex: If the input is:

0
(or less than 0), the output is:

No change
Ex: If the input is:

45
the output is:

1 Quarter
2 Dimes
"""

total_change = int(input())

if total_change >= 1:
    dollars = total_change // 100
    total_change %= 100
    quarters = total_change // 25
    total_change %= 25
    dimes = total_change // 10
    total_change %= 10
    nickels = total_change // 5
    total_change %= 5
    pennies = total_change

    if dollars == 1:
        print(dollars, "Dollar")
    elif dollars > 1:
        print(dollars, "Dollars")
    if quarters == 1:
        print(quarters, "Quarter")
    elif quarters > 1:
        print(quarters, "Quarters")
    if dimes == 1:
        print(dimes, "Dime")
    elif dimes > 1:
        print(dimes, "Dimes")
    if nickels == 1:
        print(nickels, "Nickel")
    elif nickels > 1:
        print(nickels, "Nickels")
    if pennies == 1:
        print(pennies, "Penny")
    elif pennies > 1:
        print(pennies, "Pennies")
else:
    print("No change")
