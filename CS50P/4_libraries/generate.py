import random # retain scope
# from random import choice # import function explicitly

### random.choice(SEQ) ###
# coin = random.choice(["heads", "tails"])
# print(coin)

### random.randint(a,b) ###
number = random.randint(1, 10)
print(number)

### random.shuffle(x) ###
cards = ["jack", "queen", "king"]
random.shuffle(cards)
for card in cards:
    print(card)
