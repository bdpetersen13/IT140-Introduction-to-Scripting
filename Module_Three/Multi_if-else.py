"""
Write an if-else statement with multiple branches.
If year is 2101 or later, print "Distant future" (without quotes). Otherwise, if year is 2001 or greater, print "21st century". Otherwise, if year is 1901 or greater, print "20th century". Else (1900 or earlier), print "Long ago".

Sample output with input: 1776
Long ago
"""

year = int(input())


if year >= 2101:
    print("Distant future")
elif year >= 2001:
    print("21st century")
elif year >= 1901:
    print("20th century")
else:
    print("Long ago")
