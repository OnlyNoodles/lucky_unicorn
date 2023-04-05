"""Component 3 (random tokens) v2
Calculate user balance based on random selection of tokens"""

import random
tokens = ["zebra", "horse", "donkey", "unicorn"]
balance = 100


# Testing loop to generate 20 tokens
for items in range(20):
    token = random.choice(tokens)
    print(token, end='\t')  # Can wrap output making it easier to screenshot


# Adjust balance
    if token == "unicorn":
        balance += 4
    elif token == "donkey":
        balance -= 1
    else:
        balance -= 0.50


# Output
print(f"Token: {token}. Balance: ${balance}")
