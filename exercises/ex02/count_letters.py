"""Counting letters in a string."""

__author__ = "730330121"


# Begin your solution here...
special_letter: str = (input("What letter do you want to search for? "))
word_in_question: str = (input("Enter a word: "))
count_of_letter: int = 0
i: int = 0

while i < int(len(word_in_question)):
    if special_letter == word_in_question[i]:
        count_of_letter = count_of_letter + 1
    i = i + 1

print("Count: " + str(count_of_letter))