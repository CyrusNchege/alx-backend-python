#!/usr/bin/env python3
""" Function that takes string and int and return tupple"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Creates a tuple with string k and the square of int/float v as a float."""
    return (k, float(v**2))
