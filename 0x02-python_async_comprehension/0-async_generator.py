#!/usr/bin/env python3
"""A Python module to loop 10 times asynchronously."""

import random
import asyncio
from typing import Generator

async def async_generator() -> Generator[float, None, None]:
    """
    async_generator - Generate random numbers asynchronously.

    This coroutine loops 10 times, waiting for 1 second between each yield,
    and yields random numbers between 0 and 10.

    Returns:
        Generator[float, None, None]: A generator of random float values.
    """
    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
