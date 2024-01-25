#!/usr/bin/python3
"""
LIFO caching
"""

from base_caching import BaseCaching

class LIFOCache(BaseCaching):
    """
    LIFO Cache
    """

    def __init__(self):
        """Constructor"""
        super().__init__()
        self.remove = None

    def put(self, key, item):
        """Add key-value pair to the cache"""
        if key and item:
            self.cache_data[key] = item
            self.remove_if_needed()

    def get(self, key):
        """Get value associated with key"""
        return self.cache_data.get(key, None)

    def remove_if_needed(self):
        """Check and evict items if the cache exceeds its size"""
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            removed_key = self.remove
            self.cache_data.pop(removed_key)
            print("DISCARD: {}".format(removed_key))
            self.remove = next(reversed(self.cache_data), None)