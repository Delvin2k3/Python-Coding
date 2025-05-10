# import random

# def rollDice():
#     return random.randint(1,6)

# number = rollDice()
# print(number)


import random 
import math

def rollDice():
    return math.floor(random.random()*6) + 1

number = rollDice()
print(number)