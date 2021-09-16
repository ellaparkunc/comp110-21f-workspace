"""Finding duplicate letters in a word."""

__author__ = "730330121"

word: str = input("Enter a word: ")
i: int = 0
count: int = 0

while i < len(word):
    n: int = 0
    while n < len(word):
        if word[i] == word[n]:
            count = count + 1
        n += 1

    i = i + 1

count = count - len(word)
if count > 0:
    print("Found duplicate: True")
else:
    print("Found duplicate: False")