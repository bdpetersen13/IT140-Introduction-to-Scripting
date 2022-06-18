"""
Assign decoded_tweet with user_tweet, replacing any occurrence of 'TTYL' with 'talk to you later'.

Sample output with input: 'Gotta go. I will TTYL.'
Gotta go. I will talk to you later.
"""

user_tweet = input()

decoded_tweet =  user_tweet.replace('TTYL','talk to you later')
print(decoded_tweet)
