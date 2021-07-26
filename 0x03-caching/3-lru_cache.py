#!/usr/bin/python3
""" LRU Caching modules
"""

from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Cache system, inherts from BaseCaching
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ Add item in the cache using FIFO
        """
        keyss = self.cache_data.keys()

        if key and item:

            if key in keyss:
                self.cache_data.pop(key)

            elif len(keyss) >= self.MAX_ITEMS and \
                    key not in keyss:

                item = list(keyss)[0]

                self.cache_data.pop(item)

                print("DISCARD: {}".format(item))

            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """

        if key is None:

            return None

        itemKeys = self.cache_data.keys()

        if key in itemKeys:

            value = self.cache_data.pop(key)

            self.cache_data[key] = value

        return self.cache_data.get(key, None)
