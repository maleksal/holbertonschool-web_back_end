#!/usr/bin/env python3
"""
Async comprehension Module.
"""
import asyncio
from typing import List
import random


async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Collect 10 random numbers using an async comprehensing over async_generator
    """
    return [i async for i in async_generator()]
