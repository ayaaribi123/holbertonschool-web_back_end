#!/usr/bin/env python3
"""
measure_runtime should measure
the total runtime and return it.
"""
import time
import asyncio
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    execute async_comprehension
    measure time.
    """
    first = time.time()
    await asyncio.gather(async_comprehension())
    second = time.time()
    result = second - first
    return result
