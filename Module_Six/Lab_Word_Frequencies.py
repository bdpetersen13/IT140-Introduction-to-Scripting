"""

Write a program that reads a list of words. Then, the program outputs those words and their frequencies.

Ex: If the input is:

hey hi Mark hi mark
the output is:

hey 1
hi 2
Mark 1
hi 2
mark 1
"""

user_sentence = input()
from collections import Counter

for word in user_sentence.split():
    print(f"{word} {Counter(user_sentence.split())[word]}")
