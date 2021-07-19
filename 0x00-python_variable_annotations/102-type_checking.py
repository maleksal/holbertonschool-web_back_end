#!/usr/bin/env python3
'''   type checking using mypy
'''
from typing import Tuple, List, Any


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    """[zoom_array]
    Args:
        lst (tuple): Tuple
        factor (int, optional): [factor]
    Returns:
        List: [returned_list]
    """
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(tuple(array))

zoom_3x = zoom_array(tuple(array), int(3.0))