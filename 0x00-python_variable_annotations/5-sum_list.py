#!/usr/bin/env python3
"""A function to calculate the sum of a list of floats."""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Calculate the sum of a list of floats.

    Args:
        input_list (List[float]): A list of floats to be summed.

    Returns:
        float: The sum of the floats in the input list.
    """
    return sum(input_list) if input_list is not None else 0
