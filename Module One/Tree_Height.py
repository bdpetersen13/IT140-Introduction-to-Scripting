"""
Simple geometry can compute the height of an object from the object's shadow length and shadow angle using the formula: tan(angleElevation) = treeHeight / shadowLength. Given the shadow length and angle of elevation, compute the tree height.

Sample output with inputs: 0.4 17.5
Tree height: 7.398881327917831
"""

import math

tree_height = 0.0

angle_elev  = float(input())
shadow_len  = float(input())

tree_height = math.tan(angle_elev) * shadow_len

print('Tree height:', tree_height)
