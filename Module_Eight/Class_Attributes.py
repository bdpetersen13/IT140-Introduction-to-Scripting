"""
Print the attributes of the InventoryTag object red_sweater.

Sample output for the given program with inputs: 314 500
ID: 314
Qty: 500
"""

class InventoryTag:
    def __init__(self):
        self.item_id = 0
        self.quantity_remaining = 0

red_sweater = InventoryTag()
red_sweater.item_id = int(input())
red_sweater.quantity_remaining = int(input())

print("ID:", red_sweater.item_id)
print("Qty:",red_sweater.quantity_remaining)
