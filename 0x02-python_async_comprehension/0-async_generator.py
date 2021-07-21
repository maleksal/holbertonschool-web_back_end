#!/usr/bin/env python3
"""
Async generator coroutine
"""
import asyncio
from typing import AsyncGenerator
import random


async def async_generator() -> AsyncGenerator[float, None, None]:
    """
    Loop 10 times, wait 1 second, then yield a random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
