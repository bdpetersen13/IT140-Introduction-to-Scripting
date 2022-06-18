"""
A cashier distributes change using the maximum number of five-dollar bills, followed by one-dollar bills. Write a single statement that assigns num_ones with the number of distributed one-dollar bills given amount_to_change. Hint: Use %.

Sample output with input: 19
Change for $ 19
3 five dollar bill(s) and 4 one dollar bill(s)
"""

amount_to_change = int(input())

num_fives = amount_to_change // 5

num_ones = amount_to_change % 5

print('Change for $', amount_to_change)
print(num_fives, 'five dollar bill(s) and', num_ones, 'one dollar bill(s)')
