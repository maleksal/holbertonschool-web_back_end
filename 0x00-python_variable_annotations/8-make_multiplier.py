#!/usr/bin/env python3
"""make_multiplier Module"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Takes a multiplier and returns a function.
    :param multiplier: float
    :return: Callable[[float], float]
    """
    return lambda x: float(x * multiplier)
