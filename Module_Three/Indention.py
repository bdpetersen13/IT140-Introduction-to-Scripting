"""
Retype the below code. Fix the indentation as necessary to make the program work.
    if 'New York' in temperatures:
        if temperatures['New York'] > 90:
        print('The city is melting!')
        else:
            print('The temperature in New York is', temperatures['New York'])
else:
        print('The temperature in New York is unknown.')
Sample output with input: 105

The city is melting!
"""

temperatures = {
    'Seattle': 56.5,
    'New York': float(input()),
    'Kansas City': 81.9,
    'Los Angeles': 76.5
}

if 'New York' in temperatures:
    if temperatures['New York'] > 90:
        print("The city is melting!")
    else:
        print("The temperature in New York is", temperatures['New York'])
else:
    print("The temperature in New York is unknown")
