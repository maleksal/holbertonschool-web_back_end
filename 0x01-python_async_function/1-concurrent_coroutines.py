#!/usr/bin/env python3
"""async Module"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns the list of all the delays (float values)."""
    task_lst = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    return [await i for i in asyncio.as_completed(task_lst)]
