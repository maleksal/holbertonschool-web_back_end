#!/usr/bin/env python3
"""to_kv Module"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    :param k: string
    :param v: int OR float
    :return: (str, square(v) -> float)
    """
    return k, float(v ** 2)
