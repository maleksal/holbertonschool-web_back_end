#!/usr/bin/python3
""" LIFO cache module
"""

BaseCashing = __import__('base_caching').BaseCaching


class LIFOCache(BaseCashing):
    """ Cache system, inherts from BaseCaching
    """

    def __init__(self) -> None:
        super().__init__()

    def put(self, key, item):
        """ Add item in the cache using FIFO
        """
        dict_keys = list(self.cache_data.keys())

        if key and item:

            if len(self.cache_data) >= BaseCashing.MAX_ITEMS and \
                    key not in dict_keys:

                ikey = dict_keys[-1]
                print("DISCARD:", ikey)
                self.cache_data.pop(ikey)

            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        return (
            self.cache_data[key]
            if key and key in self.cache_data.keys() else None
        )
