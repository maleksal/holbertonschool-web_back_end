#!/usr/bin/env python3
"""
Helper function module.
"""


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of size two containing a start index and an end index.
    """
    s, e = page * page_size, page * page_size
    return (s - page_size, e)
