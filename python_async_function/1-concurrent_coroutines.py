#!/usr/bin/env python3
"""
Import wait_random from the previous python
file that you've written and write an async
routine called wait_n that takes in 2 int arguments
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
    return sorted(list)
