#!/usr/bin/python3
"""
MRU Caching
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    Class that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        super().__init__()

    def _update_order(self, key):
        """Update the order of keys to represent MRU"""
        if key in self.cache_data:
            del self.cache_data[key]
        self.cache_data[key] = None

    def put(self, key, item):
        """Add key-value pair to the cache"""
        if key and item:
            self._update_order(key)
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded_key = next(iter(self.cache_data))
                print("DISCARD:", discarded_key)
                del self.cache_data[discarded_key]
            self.cache_data[key] = item

    def get(self, key):
        """Get value associated with key"""
        return self.cache_data.get(key, None)
