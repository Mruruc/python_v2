# Random Numbers

# Python does not have a random() function to make a random number,
# but Python has a built-in module called random that can be used to make random numbers:

import random

# randrange()	Returns a random number between the given range
numBetween1to10 = random.randrange(1, 10)
print(numBetween1to10)

# choice()	Returns a random element from the given sequence:
fruits = ['Apple', 'Banana', 'Chery', 'Melon']

print(random.choice(fruits))
