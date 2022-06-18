"""
Assign avg_owls with the average owls per zoo. Print avg_owls as an integer.

Sample output for inputs: 1 2 4
Average owls per zoo: 2
"""

avg_owls = 0.0

num_owls_zooA = int(input())
num_owls_zooB = int(input())
num_owls_zooC = int(input())

avg_owls = (num_owls_zooA + num_owls_zooB + num_owls_zooC) / 3

print('Average owls per zoo:', int(avg_owls))
