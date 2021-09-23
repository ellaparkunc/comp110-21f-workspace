"""List utility functions."""

__author__ = "730330121"


# TODO: Implement your functions here.

def all(haystack: list[int], needle: int) -> bool:
    """Function Called all which you give a list of ints and tells you if the "needle" (specific variable) is equal to every int in "haystack" (list)."""
    i: int = 0
    if haystack == []:
        return False
    while i < len(haystack):
        if haystack[i] != needle:
            return False
        i += 1
    return True


def is_equal(first_list: list[int], second_list: list[int]) -> bool:
    """Function which tells you if two lists are exactly equal."""
    if len(first_list) != len(second_list):
        return False
    if first_list == [] and second_list != []:
        return False
    if second_list == [] and first_list != []:
        return False
    i: int = 0
    count: int = 0
    while i < len(first_list):
        if first_list[i] != second_list[i]:
            count += 1
        i += 1
    if count > 0:
        return False
    return True


def max(ocean: list[int]) -> biggest_fish:
    """What is the largest number in this set."""
    if len(ocean) == 0:
        raise ValueError("max() arg is an empty List")
    i: int = 0
    count: int = 0
    while i < len(ocean):
        if ocean[i] > ocean[j]:
            count += 1




if __name__ == "__main__":
    print(max([1, 2, 3]))