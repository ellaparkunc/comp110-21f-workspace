"""Utility class for numerical operations."""

from __future__ import annotations

from typing import Union

__author__ = "730330121"


class Simpy:
    """Models simpy???"""

    # Attribute Definitions
    values: list[float]

    def __init__(self, values: list[float]):
        """Constructor definition for initiation of my attribute."""
        self.values = values

    def __str__(self) -> str:
        """Method which converts my values to strings."""
        values = self.values
        string: str = (f"Simpy{values}")
        return string
    
    def fill(self, filler: float, N: int) -> None:
        