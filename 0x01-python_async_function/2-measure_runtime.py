#!/usr/bin/env python3
"""Measure the runtime"""
import asyncio
from time import perf_counter
wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int = 0, max_delay: int = 10) -> float:
    """measure_time: function that measures the total execution time for
        wait_n(n, max_delay), and returns total_time / n. Your function should
        return a float.
    """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    end = perf_counter()
    return (end - start) / n