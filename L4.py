from random import choice

coin = choice(["heads", "tails"])
print(coin)



from random import randint

number = randint(1, 10)
print(number)



from random import shuffle
cards = ['jack', 'queen','king','ace']
shuffle(cards)
for card in cards:
    print(card)