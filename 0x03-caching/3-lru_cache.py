#!/usr/bin/python3
""" LRU Caching modules
"""
from collections import OrderedDict
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """ Cache system, inherts from BaseCaching
    """

    def __init__(self):
        """ Initiliaze
        """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add item in the cache using FIFO
        """

        if key and item:

            self.cache_data[key] = item

        if len(self.cache_data.keys()) > BaseCaching.MAX_ITEMS:

            ritem = list(self.cache_data.popitem(last=False))[0]

            print("DISCARD:", ritem)

            self.cache_data.move_to_end(key, last=True)

    def get(self, key):
        """ Get an item by key
        """
        if key in self.cache_data.keys():

            self.cache_data.move_to_end(key, last=True)

            return self.cache_data[key]

        return None
