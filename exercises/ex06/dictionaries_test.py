"""Unit tests for dictionary functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex06.dictionaries import invert, favorite_color, count

__author__ = "730330121"

from exercises.ex06.dictionaries import invert
from exercises.ex06.dictionaries import favorite_color
from exercises.ex06.dictionaries import count


def test_invert_normal() -> None:
    """Tests normal use with numbers and letters."""
    given: dict[str, str] = {"0": "a", "2": "b"}
    assert invert(given) == {"a": "0", "b": "2"}


def test_invert_letters() -> None:
    """Tests normal use with only numbers."""
    given: dict[str, str] = {"z": "a", "x": "b"}
    assert invert(given) == {"a": "z", "b": "x"}


def test_invert_edge() -> None:
    """Tests if invert is given an empty dictionary."""
    given: dict[str, str] = {}
    assert invert(given) == {}


def test_favorite_color() -> None:
    """Tests if names of TA's and Professors and thier favorite colors gives most common color."""
    xs: dict[str, str] = {"Marc": "yellow", "Ezri": "blue", "Kris": "blue"}
    assert favorite_color(xs) == "blue"


def test_favorite_color_family() -> None:
    """Tests if it will find my family's most common favorite color."""
    color: dict[str, str] = {"Dad": "chartruse", "Westley": "teal", "Ella": "lavendar", "Catherine": "teal"}
    assert favorite_color(color) == "teal"


def test_favorite_color_edge() -> None:
    """If there is a tie for most common favorite color, will give the color that came first in the dictionary."""
    xs: dict[str, str] = {"Dad": "chartruse", "Westley": "teal", "Ella": "lavendar", "Catherine": "teal", "David": "lavendar"}
    assert favorite_color(xs) == "teal"


def test_count_normal() -> None:
    """Tests if count will count the number each element is present in the list."""
    z: list[str] = ["red", "yellow", "blue", "yellow"]
    assert count(z) == {'red': 1, 'yellow': 2, 'blue': 1}


def test_count_all_one() -> None:
    """Tests if count will count the numbers of the elements, even if there is just one of each."""
    z: list[str] = ["red", "yellow", "blue", "green"]
    assert count(z) == {'red': 1, 'yellow': 1, 'blue': 1, 'green': 1}


def test_count_empty() -> None:
    """Tests if count is given empty list."""
    z: list[str] = []
    assert count(z) == {}
