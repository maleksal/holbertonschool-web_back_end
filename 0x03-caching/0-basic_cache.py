#!/usr/bin/python3
""" Basic cache module
"""

BaseCashing = __import__('base_caching').BaseCaching


class BasicCache(BaseCashing):
    """ Cache system, inherts from BaseCaching
    """

    def __init__(self) -> None:
        super().__init__()

    def put(self, key, item):
        """ Add item in the cache
        """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        return (
            self.cache_data[key]
            if key and key in self.cache_data.keys() else None
        )
