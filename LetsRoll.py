# Wade Polo 3/10/14
# Let's Roll
# Reports the results of rolling a single die 6,000,000 times

import random

random.seed()

one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
diceRolls = 0

while diceRolls < 6000000:
    diceRolls = diceRolls + 1
    roll = random.randint(1,6)
    if roll == 1:
        one = one + 1
    elif roll == 2:
        two = two + 1
    elif roll == 3:
        three = three + 1
    elif roll == 4:
        four = four + 1
    elif roll == 5:
        five = five + 1
    else:
        six = six + 1

print('Here are the results of 6,000,000 rolls of a six sided die using a random seed:')
print(format(one,',d'),'ones were rolled.')
print(format(two,',d'),'twos were rolled.')
print(format(three,',d'),'threes were rolled.')
print(format(four,',d'),'fours were rolled.')
print(format(five,',d'),'fives were rolled.')
print(format(six,',d'),'sixes were rolled.')
