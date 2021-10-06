"""List utility functions part 2."""

__author__ = "730330121"

# Define your functions below


def only_evens(xs: list[int]) -> list[int]:
    """Given a list will spit out the list of only integers aka will ask is odd? then that number."""
    i: int = 0
    while i < len(xs):
        if xs[i] % 2 != 0:
            xs.pop(i)
        else:
            i += 1
    return(xs)


def sub(xs: list[int], start: int, end: int) -> list[int]:
    new: list[int] = []
    while start < end:
        new.append(xs[start])
        start += 1
    print(new)
    return(new)


if __name__ == "__main__":
    sub([10, 20, 30, 40], 1, 3)