"""
Write a program that takes a date as input and outputs the date's season. The input is a string to represent the month and an int to represent the day.

Ex: If the input is:

April
11
the output is:

Spring
In addition, check if the string and int are valid (an actual month and day).

Ex: If the input is:

Blue
65
the output is:

Invalid
The dates for each season are:
Spring: March 20 - June 20
Summer: June 21 - September 21
Autumn: September 22 - December 20
Winter: December 21 - March 19
"""

input_month = input()
input_day = int(input())
months = ('January', 'Feburary', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

if not (input_month in months):
    print('Invalid')

if input_day < 0:
    print('Invalid')

elif input_day > 30:
    print('Invalid')

if input_month in ('January', 'Feburary', 'March'):
    season = 'Winter'

elif input_month in ('April', 'May', 'June'):
    season = 'Spring'

elif input_month in ('July', 'August', 'September'):
    season = 'Summer'

elif input_month in ('October', 'November'):
    season = 'Autumn'

if (input_month == 'March') and (input_day >= 20):
    season = 'spring'

elif (input_month == 'June') and (input_day >= 21):
    season = 'Summer'

elif (input_month == 'September') and (input_day >= 22):
    season = 'Autumn'

elif (input_month == 'December') and (input_day >= 21):
    season = 'Winter'

print(season)
