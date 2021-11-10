"""Utility functions."""

__author__ = "123456789"

# Define your functions below
# This is the Python module where you will implement utility functions for working with data.

from csv import DictReader


def read_csv_rows(filename: str) -> list[dict[str, str]]:
    """Read the rows of a csv into a 'table'."""
    result: list[dict[str, str]] = []

    # Open a handle to the data file
    file_handle = open(filename, "r", encoding="utf8")

    # Prepre to read the data file as a CSV rather than just strings
    csv_reader = DictReader(file_handle)
    
    # Read each row of the CSV line-by-line
    for row in csv_reader:
        result.append(row)
    
    # Close the file when we're done, to free its resources.
    file_handle.close()
    return result


def column_values(table: list[dict[str, str]], column: str) -> list[str]:
    """Produce a list[str] of all values in a single column."""
    result: list[str] = []
    for row in table:
        item: str = row[column]
        result.append(item)
    return result


def columnar(row_table: list[dict[str, str]]) -> dict[str, list[str]]:
    """Transform a row-oriented table to a column-oriented table."""
    result: dict[str, list[str]] = {}

    first_row: dict[str, str] = row_table[0]
    for column in first_row:
        result[column] = column_values(row_table, column)
        
    return result


ayo: dict[str, list[str]] = {"school": ["UNC", "NCSU", "Duke"], "mascot": ["Rameses", "Wolf", "A Literal Devil"], "founded": ["1789", "1887", "1838"]}


def head(given: dict[str, list[str]], N: int) -> dict[str, list[str]]:
    """Views first N rows of a column-based table."""
    answer: dict[str, list[str]] = {}
    
    for column in given:
        if N >= len(given[column]):
            return(given)
        listy: list[str] = []
        i: int = 0
        while i < N:
            listy.append(given[column][i])
            i += 1
        answer[column] = listy
    return(answer)


def select(hello: dict[str, list[str]], xs: list[str]) -> dict[str, list[str]]:
    """To produce a column-based table with only a specific subset of the original columns.""" 
    answer_dict: dict[str, list[str]] = {}
    for column_name in xs:
        answer_dict[column_name] = hello[column_name]
    return(answer_dict)


def concat(first: dict[str, list[str]], second: dict[str, list[str]]) -> dict[str, list[str]]:
    """To combine two column-based dictionaries into one."""
    combined: dict[str, list[str]] = {}
    for column in first:
        combined[column] = first[column]
    for column in second:
        if column in first:
            combined[column] = first[column] + second[column]
        else:
            combined[column] = second[column]
    return(combined)