"""An exercise in remainders and boolean logic."""

__author__ = "730330121"


# Begin your solution here...
deciding_integer: int = int(input("Enter an integer! "))

if deciding_integer % 7 == 0:
    if deciding_integer % 2 == 0:
        print("TAR HEELS")
    else:
        print("HEELS")
else:
    if deciding_integer % 2 == 0:
        print("TAR")
    else:
        print("CAROLINA")