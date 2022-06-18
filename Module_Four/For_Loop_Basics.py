"""
Write an expression to print each price in stock_prices.

Sample output with inputs: 34.62 76.30 85.05
$ 34.62
$ 76.30
$ 85.05
"""

# NOTE: The following statement converts the input into a list container
stock_prices = input().split()

for price in stock_prices:
    print('$', price)
