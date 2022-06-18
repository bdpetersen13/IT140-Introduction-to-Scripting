"""
Write two statements to read in values for my_city followed by my_state. Do not provide a prompt. Assign log_entry with current_time, my_city, and my_state. Values should be separated by a space. Sample output for given program if my_city is Houston and my_state is Texas:
2014-07-26 02:12:18: Houston Texas
Note: Do not write a prompt for the input values.
"""

current_time = '2014-07-26 02:12:18:'
my_city = ''
my_state = ''
log_entry = ''

my_city = input("")
my_state = input("")
log_entry = current_time + ' ' + my_city + ' ' + my_state

print(log_entry)
