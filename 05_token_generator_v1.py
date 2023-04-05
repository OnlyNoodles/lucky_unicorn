"""Component 3 (random tokens) v1
Generates random choice of token in random order"""

import random
tokens = ["zebra", "horse", "donkey", "unicorn"]


# Testing loop to generate 20 tokens
for items in range(20):
    token = random.choice(tokens)
    print(token, end='\t')  # Can wrap output making it easier to screenshot
