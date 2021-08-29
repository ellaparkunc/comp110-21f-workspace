"""Recieving a True or False Answer to a Math Question Plus Relational Operators."""

__author__ = "730330121"

left: int = int(input("What is the left number? "))
right: int = int(input("What is the right number? "))
print("Left-hand side: " + str(left))
print("Right-hand side: " + str(right))

print(str(left) + " < " + str(right) + " is " + str(bool(left < right)))
print(str(left) + " >= " + str(right) + " is " + str(bool(left >= right)))
print(str(left) + " == " + str(right) + " is " + str(bool(left == right)))
print(str(left) + " != " + str(right) + " is " + str(bool(left != right)))