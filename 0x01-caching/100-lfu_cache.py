#!/usr/bin/env python3
""" LFUCache module with caching system"""

from base_caching import BaseCaching
from collections import OrderedDict


class LFUCache(BaseCaching):
    """LFUCache impls caching system with LFU eviction policy and LRU."""

    def __init__(self):
        """Initialize LFUCache by calling parent initializer."""
        super().__init__()
        self.frequency = {}
        self.order = OrderedDict()

    def put(self, key, item):
        """Add an item to the cache using LFU eviction if needed.

        Args:
            key: The key to be assigned in cache.
            item: The item to store in cache.
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            # Update the existing item and frequency
            self.cache_data[key] = item
            self.frequency[key] += 1
            self.order.move_to_end(key)
        else
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            min_freq = min(self.frequency.values())
            lfu_keys =
            [k for k, freq in self.frequency.items() if freq == min_freq]
            lfu_lru_key = lfu_keys[0] if len(lfu_keys) ==
            1 else next(k for k in self.order if k in lfu_keys)
            print(f"DISCARD: {lfu_lru_key}")
            del self.cache_data[lfu_lru_key]
            del self.frequency[lfu_lru_key]
            del self.order[lfu_lru_key]

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.order[key] = None

        def get(self, key):
            """Retrieve item from cache by key and update its access.

        Args:
            key: The key associated with the item.

        Returns:
            Value in cache_data, or None if key is None or not in cache.
        """
        if key is None or key not in self.cache_data:
            return None

        self.frequency[key] += 1
        self.order.move_to_end(key)
        return self.cache_data[key]
