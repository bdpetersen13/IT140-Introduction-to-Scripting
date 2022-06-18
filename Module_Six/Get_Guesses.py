"""
Write a loop to populate the list user_guesses with a number of guesses. The variable num_guesses is the number of guesses the user will have, which is read first as an integer. Read each guess (an integer) one at a time using int(input()).

Sample output with input:
3 9 5 2
user_guesses: [9, 5, 2]
"""

num_guesses = int(input())
user_guesses = []

for i in range(num_guesses):
    user_guesses.append(int(input()))

print('user_guesses:', user_guesses)
