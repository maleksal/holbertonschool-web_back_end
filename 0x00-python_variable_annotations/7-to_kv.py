#!/usr/bin/env python3
"""to_kv Module"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> tuple:
    """
    :param k: string
    :param v: int OR float
    :return: (str, square(v) -> float)
    """
    from math import sqrt
    return Tuple[k, float(sqrt(v))]
