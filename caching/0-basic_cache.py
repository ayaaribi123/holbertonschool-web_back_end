#!/usr/bin/python3
"""
Basic dictionary
"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache
    """

    def put(self, key, item):
        """Assign to the dictionary"""
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Return the value linked to key"""
        return self.cache_data.get(key, None)
