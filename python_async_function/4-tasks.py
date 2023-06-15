#!/usr/bin/env python3
"""
module for the wait
"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    same as identical to wait_n
    """
    list = []
    for l in range(n):
        list.append(await task_wait_random(max_delay))
    return sorted(list)
