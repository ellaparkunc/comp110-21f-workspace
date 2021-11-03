"""Practice with dictionaries."""

__author__ = "730330121"

# Define your functions below

given: dict[str, str] = {"0": "a", "1": "b"}


def invert(given: dict[str, str]) -> dict[str, str]:
    """Inverts a dictionary."""
    """What i want to do: take a and rename each """
    """Turning a dictionary into a list."""
    inverted: dict[str, str] = {}
    c: list[str] = []
    for key in given:
        c.append(given[key])

    i: int = 0
    count: int = 0

    while i < len(c):
        n: int = 0
        while n < len(c):
            if c[i] == c[n]:
                count = count + 1
            n += 1
        i = i + 1
    count = count - len(c)
    if count > 0:
        raise KeyError("KeyError")
        
    """The actual inversion."""
    for key in given:
        inverted[given[key]] = key
    print(inverted)
    return inverted


a: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}


def favorite_color(known: dict[str, str]) -> str:
    """When given a dictionary of names and favorite colors, gives the most common colors."""
    easier: list[str] = []
    for name in known:
        easier.append(known[name])

    counter: dict[str, int] = {}
    for key in easier:
        counter[key] = 0

    i: int = 0
    while i < len(easier):
        counter[easier[i]] += 1
        i = i + 1

    biggest: int = 0
    answer: str = "hi"
    for color in counter:
        if counter[color] > biggest:
            biggest = counter[color]
            answer = color
    print(answer)
    return(answer)


z: list[str] = ["red", "yellow", "blue", "yellow"]


def count(silly: list[str]) -> dict[str, int]:
    """Counts the number of times a list's item is present in the list."""
    work: dict[str, int] = {}
    for key in silly:
        work[key] = 0
    i: int = 0
    while i < len(silly):
        work[silly[i]] += 1
        i += 1
    
    print(work)
    return(work)


if __name__ == "__main__":
    invert(given)
    favorite_color(a)
    count(z)