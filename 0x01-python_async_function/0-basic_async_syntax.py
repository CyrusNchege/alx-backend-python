#!/usr/bin/env python3
""" Basic async """
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """ wait_random

    Args:
        max_delay (int, optional): [max delay]. Defaults to 10.

    Returns:
        float: [random delay]
    """
    random_delay = random.uniform(0, max_delay)
    await asyncio.sleep(random_delay)
    return random_delay 