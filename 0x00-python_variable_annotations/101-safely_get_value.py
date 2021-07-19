#!/usr/bin/env python3
"""TASK 11 Module"""
from typing import Union, TypeVar, Any, Mapping


typ = TypeVar["T"]


def safely_get_value(dct: Mapping, key: Any, default: Union[typ, None])\
        -> Union[Any, typ]:
    """safely_get_value."""
    if key in dct:
        return dct[key]
    else:
        return default
