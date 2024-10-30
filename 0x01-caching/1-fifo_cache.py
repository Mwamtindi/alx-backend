#!/usr/bin/env python3
""" FIFOCache module with a caching system
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """FIFOCache is a caching system with FIFO eviction policy."""

    def __init__(self):
        """Initialize FIFOCache by calling parent initializer."""
        super().__init__()
        self.keys_order = []

    def put(self, key, item):
        """Add an item to cache using FIFO policy if limit is reached.

        Args:
            key: The key to be assigned in cache.
            item: The item to store in cache.
        """
        if key is None or item is None:
            return

        self.cache_data[key] = item
        if key not in self.keys_order:
            self.keys_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key = self.keys_order.pop(0)
            del self.cache_data[oldest_key]
            print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """Retrieve item from cache by key.

        Args:
            key: The key associated with the item.

        Returns:
            Value in cache_data, None if key is None or not in cache.
        """
        return self.cache_data.get(key, None)
