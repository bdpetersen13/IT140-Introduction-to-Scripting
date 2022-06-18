"""
Write a program that replaces words in a sentence. The input begins with word replacement pairs (original and replacement). The next line of input is the sentence where any word on the original list is replaced.

Ex: If the input is:

automobile car   manufacturer maker   children kids
The automobile manufacturer recommends car seats for children if the automobile doesn't already have one.
the output is:

The car maker recommends car seats for kids if the car doesn't already have one.
You can assume the original words are unique.
"""

pairs = input().split()

original = pairs[::2]
replacement = pairs[1::2]

sentence = input()

for org, repl in zip(original, replacement):
    sentence = sentence.replace(org, repl)

print(sentence)
