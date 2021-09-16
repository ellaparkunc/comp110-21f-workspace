"""Drawing forests in a loop."""

__author__ = "730330121"

# The string constant for the pine tree emoji
TREE: str = '\U0001F332'

d: int = int(input("What is the integer depth? "))
i: int = 0
the_forest: str = ""
while i < d:
    print(str(TREE) + str(TREE * i)) 
    i += 1