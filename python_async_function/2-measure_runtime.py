#!/usr/bin/env python3
"""
a measure_time function with integers n
and max_delay as arguments that measures
the total execution time for wait_n(n, max_delay),
and returns total_time / n. Your function should return a float.
"""
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int = 10) -> float:
    """
    Measure the runtime
    """

    asyncio.run(wait_n(n, max_delay))
    first = time.time()
    second = time.time()
    resualt = second - first
    return (resualt / n)
