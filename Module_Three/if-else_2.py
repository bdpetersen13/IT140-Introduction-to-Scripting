"""
Write an if-else statement for the following:
If user_tickets is less than 5, assign 1 to num_tickets. Else, assign user_tickets to num_tickets.

Sample output with input: 3
Value of num_tickets: 1
"""

user_tickets = int(input())

if user_tickets < 5:
    num_tickets = 1
else:
    num_tickets = user_tickets

print('Value of num_tickets:', num_tickets)
