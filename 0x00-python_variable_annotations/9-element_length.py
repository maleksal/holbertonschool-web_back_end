#!/usr/bin/env python3
"""element_length Module"""
from typing import List, Any, Sequence, Iterable, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """Takes a lst of args and returns list of tuples as (arg, len(arg)
    :param lst: list of items
    :return: list of tuples
    """
    return [(i, len(i)) for i in lst]
