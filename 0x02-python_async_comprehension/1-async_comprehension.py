#!/usr/bin/env python3
""" a python module to returns 10 random numbers using async comprehension"""
from typing import List
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """async_comprehension: returns 10 random numbers using async comprehension"""
    return [i async for i in async_generator()]