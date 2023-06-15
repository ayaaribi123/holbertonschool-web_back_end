#!/usr/bin/env python3
"""
an asynchronous coroutine that takes in an integer
argument (max_delay, with a default value of 10) named wait_random
that waits for a random delay between 0 and max_delay 
included and float value) seconds and eventually returns it.
"""
import asyncio
import random


async def wait_random(int = 10) -> float:
    """
    return random wait
    """
    rand = random.uniform(0, 10)
    await asyncio.sleep(rand)
    return rand
