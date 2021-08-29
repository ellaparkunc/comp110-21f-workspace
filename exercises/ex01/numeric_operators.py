"""Practice with Numeric Operators like Multiplication and Division."""

__author__ = "730330121"

left: int = int(input("What is the left number? "))
right: int = int(input("What is the right number? "))
print("Left-hand side: " + str(left))
print("Right-hand side: " + str(right))

print(str(left) + " ** " + str(right) + " is " + str(left ** right))
print(str(left) + " / " + str(right) + " is " + str(left / right))
print(str(left) + " // " + str(right) + " is " + str(left // right))
print(str(left) + " % " + str(right) + " is " + str(left % right))