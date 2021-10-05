"""Unit tests for list utility functions."""

# TODO: Uncomment the below line when ready to write unit tests
# from exercises.ex05.utils import only_evens, sub, concat

__author__ = "123456789"

from exercises.ex05.utils import only_evens


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


from exercises.ex05.utils import sub


def test_sub() -> None:
    """Tests sub."""
    example: list[int] = [10, 20, 30, 40]
    assert sub(example, 1, 3) == [20, 30]