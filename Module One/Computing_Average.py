"""
Write a single statement that assigns avg_sales with the average of num_sales1, num_sales2, and num_sales3.

Sample output with inputs: 3 4 8
Average sales: 5.00
"""

avg_sales = 0

num_sales1 = int(input())
num_sales2 = int(input())
num_sales3 = int(input())

avg_sales = (num_sales1 + num_sales2 + num_sales3) / 3

print('Average sales: {:.2f}'.format(avg_sales))
