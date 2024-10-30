#!/usr/bin/env python3
""" LIFOCache module with a caching system.
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """LIFOCache is a caching sys with a LIFO eviction policy."""

    def __init__(self):
        """Initialize LIFOCache by calling parent initializer."""
        super().__init__()
        self.keys_order = []

    def put(self, key, item):
        """Add item to cache using LIFO policy if limit reached.

        Args:
            key: The key to be assigned in cache.
            item: The item to store in cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.keys_order.remove(key)

        self.cache_data[key] = item
        self.keys_order.append(key)

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            last_key = self.keys_order.pop(-2)
            del self.cache_data[last_key]
            print(f"DISCARD: {last_key}")

    def get(self, key):
        """Retrieve item from cache by key.

        Args:
            key: The key associated with item.

        Returns:
            Value in cache_data, or None if key is None or not in cache.
        """
        return self.cache_data.get(key, None)
