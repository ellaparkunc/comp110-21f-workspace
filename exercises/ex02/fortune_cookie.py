"""Program that outputs one of at least four random, good fortunes."""

__author__ = "730330121"

# The randint function is imported from the random library so that
# you are able to generate integers at random.
# 
# Documentation: https://docs.python.org/3/library/random.html#random.randint
#
# For example, consider the function call expression: randint(1, 100)
# It will evaluate to an int value >= 1 and <= 100. 
from random import randint


# Begin your solution here...
print("Your fortune cookie says... ")

i: int = randint(1, 4)
if i == 1:
    print("You are going to become holier and more virtuous this week!")
else:
    if i == 2:
        print("Tomorrow, you will encounter an old friend.")
    else:
        if i == 3:
            print("Very soon, you will reconnect with family.")
        else: 
            if i == 4:
                print("You are going to get an A on that thing you're worried about.")

print("Now, go spread positive vibes! ")