"""Recieving a True or False Answer to a Math Question Plus Relational Operators."""

__author__ = "730330121"

left_value: int = int(input("What is the left number? "))
right_value: int = int(input("What is the right number? "))
print("Left-hand side: " + str(left_value))
print("Right-hand side: " + str(right_value))

print(str(left_value) + " < " + str(right_value) + " is " + str(bool(left_value < right_value)))
print(str(left_value) + " >= " + str(right_value) + " is " + str(bool(left_value >= right_value)))
print(str(left_value) + " == " + str(right_value) + " is " + str(bool(left_value == right_value)))
print(str(left_value) + " != " + str(right_value) + " is " + str(bool(left_value != right_value)))