#!/usr/bin/python3
"""
FIFO caching
"""


BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO Cache class
    """

    def put(self, key, item):
        """Add key-value pair to the cache"""
        if key and item:
            self.cache_data[key] = item
            self.check_size()

    def get(self, key):
        """Get value associated with key"""
        return self.cache_data.get(key, None)

    def check_size(self):
        """Check and evict items if the cache exceeds its size"""
        while len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = next(iter(self.cache_data))
            print('DISCARD:', discarded_key)
            self.cache_data.pop(discarded_key)
