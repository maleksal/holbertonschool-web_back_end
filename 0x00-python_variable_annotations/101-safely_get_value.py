#!/usr/bin/env python3
''' my TASK 11 Module
'''
from typing import Union, TypeVar, Any, Mapping

typ = TypeVar["T"]


def safely_get_value(dct: Mapping, key: Any, default: Union[typ, None])\
        -> Union[Any, typ]:
    """
    return the value.
    """
    if key in dct:
        return dct[key]
    else:
        return default
