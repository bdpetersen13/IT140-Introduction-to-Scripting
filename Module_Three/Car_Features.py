"""
Write multiple if statements. If car_year is 1969 or earlier, print "Few safety features." If 1970 or later, print "Probably has seat belts." If 1990 or later, print "Probably has antilock brakes." If 2000 or later, print "Probably has airbags." End each phrase with a period and a newline.

Sample output for input: 1995
Probably has seat belts.
Probably has antilock brakes.
"""

car_year = int(input())

if car_year <= 1969:
    print("Few safety features.")
else:
    if car_year >= 1970:
        print("Probably has seat belts.")
    if car_year >= 1990:
        print("Probably has antilock brakes.")
    if car_year > 2000:
        print("Probably has airbags.")
