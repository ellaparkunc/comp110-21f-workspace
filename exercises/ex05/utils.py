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
    """Spits out list from start index to end index, not inclusive."""
    if start < 0:
        start = 0
    if end > (len(xs) - 1):
        end = len(xs)
    new: list[int] = []
    while start < end:
        new.append(xs[start])
        start += 1
    print(new)
    return(new)


def concat(xs: list[int], ys: list[int]) -> list[int]:
    """Adds two lists together, first list and then second."""
    final: list[int] = []
    i: int = 0
    while i < len(xs):
        final.append(xs[i])
        i += 1
    i: int = 0
    while i < len(ys):
        final.append(ys[i])
        i += 1
    print(final)
    return final


if __name__ == "__main__":
    concat([10, 20, 30, 40], [1, 2, 3])