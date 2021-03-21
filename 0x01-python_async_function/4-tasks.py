#!/usr/bin/env python3
"""async Module"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns the list of all the delays (float values)."""
    task_lst = [asyncio.create_task(task_wait_random(max_delay)) for _ in range(n)]
    return [await i for i in asyncio.as_completed(task_lst)]
