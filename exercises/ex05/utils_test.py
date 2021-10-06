"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat

__author__ = "123456789"

from exercises.ex05.utils import only_evens
from exercises.ex05.utils import sub
from exercises.ex05.utils import concat


def test_only_evens_empty() -> None:
    """Tests for if the argument is empty."""
    xs: list[int] = []
    assert only_evens(xs) == []


def test_all_odds() -> None:
    """Tests for if the function is given all odd numbers."""
    xs: list[int] = [1, 3, 5]
    assert only_evens(xs) == []


def test_all_evens() -> None:
    """Tests to see if the function will leave a list alone which is already all even."""
    xs: list[int] = [2, 4, 6, 8]
    assert only_evens(xs) == [2, 4, 6, 8]


def test_sub() -> None:
    """Tests sub, normal case."""
    example: list[int] = [10, 20, 30, 40]
    assert sub(example, 1, 3) == [20, 30]


def test_negative_start_sub() -> None:
    """Tests if sub is given a negative start."""
    normal: list[int] = [1, 2, 3, 4, 5]
    assert sub(normal, -1, 3) == [1, 2, 3]


def test_large_end_sub() -> None:
    """Tests if sub is given too large of an end."""
    control: list[int] = [0, 1, 2, 3, 4]
    assert sub(control, 0, 10) == [0, 1, 2, 3, 4]


def test_empty_concat() -> None:
    """Tests if concat is given one empty list."""
    first: list[int] = []
    second: list[int] = [1, 2, 3]
    assert concat(first, second) == [1, 2, 3]


def test_normal_concat() -> None:
    """Tests a normal case of concat."""
    first: list[int] = [10, 20, 40, 30]
    second: list[int] = [1, 2, 3, 4]
    assert concat(first, second) == [10, 20, 40, 30, 1, 2, 3, 4]


def test_repeat_concat() -> None:
    """Tests if there is a repeat of a number in concat."""
    first: list[int] = [10, 20, 40, 30]
    second: list[int] = [1, 2, 3, 3]
    assert concat(first, second) == [10, 20, 40, 30, 1, 2, 3, 3]
