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
        return f"Simpy({self.values})"
    
    def fill(self, filler: float, N: int) -> None:
        """Mutates simpy's values by taking the filler value and spitting it out N times."""
        self.values = []
        i: int = 0
        while i < N:
            self.values.append(filler)
            i += 1

    def arange(self, start: float, stop: float, step: float = 1.0) -> None:
        """Increments my simpy values from start to stop by the step, if no step, it's by 1.0."""
        assert step != 0.0
        # Start an empty values list
        self.values = []
        # This function incrementing up
        if step > 0.0:
            last_value: float = start
            while last_value < stop:
                self.values.append(last_value)
                last_value += step
        else: 
            last_value: float = start
            while last_value > stop:
                self.values.append(last_value)
                last_value += start
    
    def sum(self) -> float:
        """Sums all items in 'values' attribute, by delegating task to built-in sum function."""
        return sum(self.values)

    def __add__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Doesn't mutate the object, returns new Simpy which is the sum of the old simpies or one old simpy plus the rhs value."""
        answer: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                answer.values.append(value + rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                answer.values.append(self.values[i] + rhs.values[i])
                i += 1
        return answer

    def __pow__(self, rhs: Union[float, Simpy]) -> Simpy:
        """Doesn't mutate the object, instead returns new simpy which is either the product of Simpy's or a simpy multiplied by a float."""
        answer: Simpy = Simpy([])
        if isinstance(rhs, float):
            for value in self.values:
                answer.values.append(value ** rhs)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                answer.values.append(self.values[i] ** rhs.values[i])
                i += 1
        return answer

    def __eq__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Returns a list that tells if items in each list are equal to each other at same length."""
        listy: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                if value == rhs:
                    listy.append(True)
                else:
                    listy.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                if self.values[i] == rhs.values[i]:
                    listy.append(True)
                else:
                    listy.append(False)
                i += 1
        return listy

    def __gt__(self, rhs: Union[float, Simpy]) -> list[bool]:
        """Returns a list that tells if items in the first Simpy object are greater than the items of the second Simpy object."""
        listy: list[bool] = []
        if isinstance(rhs, float):
            for value in self.values:
                if value > rhs:
                    listy.append(True)
                else:
                    listy.append(False)
        else:
            assert len(self.values) == len(rhs.values)
            i: int = 0
            while i < len(self.values):
                if self.values[i] > rhs.values[i]:
                    listy.append(True)
                else:
                    listy.append(False)
                i += 1
        return listy

    def __getitem__(self, rhs: Union[int, list[bool]]) -> Union[float, Simpy]:
        """First iteration of this function allows subscription notation to work for Simpy's."""
        """Now, it can also filter values and only return the ones in the first which are included in the second list."""
        if isinstance(rhs, int):
            answer: float = self.values[rhs]
            return(answer)
        # If we are talking about a list, and only keeping the overlap.
        else:
            S: Simpy = Simpy([])
            # Must add this value to S if what's inside the brackets results in true for a certain value in self.
            i: int = 0
            while i < len(self.values):
                # before i had if rhs[i] == True:
                if rhs[i]:
                    S.values.append(self.values[i])
                i += 1
            return(S)
    # if __name__ == "__main__":
    #     a = Simpy([1.0, 2.0, 3.0, 4.0, 2.0, 1.0])
    #     b = a[a > 2.0]