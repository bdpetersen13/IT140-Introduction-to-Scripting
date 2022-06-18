"""
Assign sub_lyric by slicing rhyme_lyric from start_index to end_index which are given as inputs.

Sample output with inputs: 4 7
cow
"""

start_index = int(input())
end_index = int(input())
rhyme_lyric = 'The cow jumped over the moon.'
sub_lyric = rhyme_lyric[start_index: end_index]
print(sub_lyric)
