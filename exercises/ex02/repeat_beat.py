"""Repeating a beat in a loop."""

__author__ = "730330121"


# Begin your solution here...
beat_to_repeat: str = input("What beat do you want to repeat? ")
number_of_repeats: int = int(input("How many times do you want to repeat it? "))
i: int = 0
final_solution: str = beat_to_repeat

if number_of_repeats > 0:
    while i < (number_of_repeats - 1):
        final_solution = final_solution + " " + beat_to_repeat
        i = i + 1
    print(final_solution)
else: 
    print("No beat...")
