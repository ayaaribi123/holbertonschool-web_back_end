#!/usr/bin/env python3
"""
module wait_random
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """
    return list of wait_random
    """
    list = []
    for l in range(n):
        list.append(await wait_random(max_delay))
    return list
