"""
Assign point_dist with the distance between point (x1, y1) and point (x2, y2). The calculation is: Distance = SquareRootOf( (x2 - x1)2 + (y2 - y1)2 ).

Sample output with inputs: 1.0 2.0 1.0 5.0
Points distance: 3.0
"""

import math

point_dist = 0.0

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

point_dist = math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

print('Points distance:', point_dist)
