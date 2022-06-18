"""
Define a named tuple Player that describes an athlete on a sports team. Include the fields name, number, position, and team.
"""

from collections import namedtuple

Player = namedtuple('Plater', ['name', 'number', 'position', 'team'])

cam = Player('Cam Newton', '1', 'Quarterback', 'Carolina Panthers')
lebron = Player('Lebron James', '23', 'Small forward', 'Los Angeles Lakers')

print(cam.name + '(#' + cam.number + ')' + ' is a ' + cam.position + ' for the ' + cam.team + '.')
print(lebron.name + '(#' + lebron.number + ')' + ' is a ' + lebron.position + ' for the ' + lebron.team + '.')
