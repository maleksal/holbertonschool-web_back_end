#!/usr/bin/env python3
"""async Module"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """waits for a random delay between 0 and max_delay"""
    r = random.random() * max_delay
    await asyncio.sleep(r)
    return r
