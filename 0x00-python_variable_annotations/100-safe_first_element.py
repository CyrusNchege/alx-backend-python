#!/usr/bin/env python3
""" Safely retrieves the first element"""
from typing import Sequence, Any, Union, Optional


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely retrieves the first element from a sequence.

    Args:
        lst (Sequence[Any]): A sequence (e.g., list, tuple) containing elements of any type.

    Returns:
        Union[Any, None]: The first element from the sequence if it exists, or None if the sequence is empty.
    """
    if lst:
        return lst[0]
    else:
        return None
