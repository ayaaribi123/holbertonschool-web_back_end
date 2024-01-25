#!/usr/bin/python3
"""
LRU Caching
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    Class that inherits from BaseCaching and is a caching system
    """

    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """Add key-value pair to the cache"""
        if key and item:
            self.cache_data[key] = item
            self.order.append(key)
            self._evict_if_needed()

    def get(self, key):
        """Get value associated with key"""
        if key is None or key not in self.cache_data:
            return None

        value = self.cache_data[key]
        self.order.remove(key)
        self.order.append(key)
        return value

    def _evict_if_needed(self):
        """Evict items if the cache exceeds its size"""
        while len(self.order) > BaseCaching.MAX_ITEMS:
            discarded_key = self.order.pop(0)
            print("DISCARD:", discarded_key)
            del self.cache_data[discarded_key]
