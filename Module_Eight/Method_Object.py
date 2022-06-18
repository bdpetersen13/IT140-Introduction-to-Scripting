"""
Define the method object inc_num_kids() for PersonInfo. inc_num_kids increments the member data num_kids.

Sample output for the given program with one call to inc_num_kids():
Kids: 0
New baby, kids now: 1
"""

class PersonInfo:
    def __init__(self):
        self.num_kids = 0

    # FIXME: Write inc_num_kids(self)

    def inc_num_kids(self):
        self.num_kids += 1

person1 = PersonInfo()

print('Kids:', person1.num_kids)
person1.inc_num_kids()
print('New baby, kids now:', person1.num_kids)
