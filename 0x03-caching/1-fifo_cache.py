#!/usr/bin/python3
""" FIFO cache module
"""

BaseCashing = __import__('base_caching').BaseCaching


class FIFOCache(BaseCashing):
    """ Cache system, inherts from BaseCaching
    """

    def __init__(self) -> None:
        super().__init__()

    def put(self, key, item):
        """ Add item in the cache using FIFO
        """
        if key and item:

            self.cache_data[key] = item

            if len(self.cache_data) > BaseCashing.MAX_ITEMS:

                ikey = list(self.cache_data)[0][0]
                del self.cache_data[ikey]
                print("DISCARD: {}".format(ikey))

    def get(self, key):
        """ Get an item by key
        """
        return (
            self.cache_data[key]
            if key and key in self.cache_data.keys() else None
        )
