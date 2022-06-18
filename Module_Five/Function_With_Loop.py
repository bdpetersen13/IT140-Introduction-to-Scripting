"""
Write a function shampoo_instructions() with parameter num_cycles. If num_cycles is less than 1, print "Too few.". If more than 4, print "Too many.". Else, print "N : Lather and rinse." num_cycles times, where N is the cycle number, followed by "Done.".

Sample output with input: 2
1 : Lather and rinse.
2 : Lather and rinse.
Done.

Hint: Define and use a loop variable.
"""

def shampoo_instructions(num_cycles):
    if num_cycles < 1:
        print("Too few.")
    elif num_cycles > 4:
        print("Too many.")
    else:
        x = 0
        while x < num_cycles:
            print(x + 1, ": Lather and rinse.")
            x = x + 1
        print("Done.")

user_cycles = int(input())
shampoo_instructions(user_cycles)
