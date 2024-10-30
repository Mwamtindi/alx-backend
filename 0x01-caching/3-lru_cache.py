#!/usr/bin/env python3
""" LRUCache module with a caching system """

from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """LRUCache is a caching system that uses the LRU eviction policy."""

    def __init__(self):
        """Initialize LRUCache by calling parent initializer."""
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """Add an item to cache using LRU policy if limit is reached.

        Args:
            key: The key to be assigned in cache.
            item: The item to store in cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            oldest_key, _ = self.cache_data.popitem(last=False)
            print(f"DISCARD: {oldest_key}")

    def get(self, key):
        """Retrieve item from cache by key and mark it as recently used.

        Args:
            key: The key associated with the item.

        Returns:
            Value in cache_data, or None if key is None or not in cache.
        """
        if key is None or key not in self.cache_data:
            return None
        self.cache_data.move_to_end(key)
        return self.cache_data[key]
