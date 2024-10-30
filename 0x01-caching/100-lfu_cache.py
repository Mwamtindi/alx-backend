#!/usr/bin/env python3
""" LFU Caching with caching machine """
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFUCache implements a caching system with LFU eviction policy"""

    def __init__(self):
        """Initialize LFUCache by calling the parent initializer"""
        super().__init__()
        self.frequencies = {}

    def put(self, key, item):
        """Add an item in cache using LFU eviction if needed"""
        if key and item:
            if key in self.cache_data:
                # Update item and frequency
                self.cache_data[key] = item
                self.frequencies[key] += 1
            else:
                # Add new item and set its frequency to 1
                if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                    # Evict least frequently used item(s)
                    min_frequency = min(self.frequencies.values())
                    keys_to_remove = [
                        k for k, v in self.frequencies.items()
                        if v == min_frequency]
                    # Remove first item that was least frequently used
                    discard = keys_to_remove[0]
                    del self.cache_data[discard]
                    del self.frequencies[discard]
                    print("DISCARD:", discard)
                self.cache_data[key] = item
                self.frequencies[key] = 1

    def get(self, key):
        """Retrieve item from cache by key and update its access"""
        if key in self.cache_data:
            # Update the frequency
            self.frequencies[key] += 1
            return self.cache_data[key]
        return None

    def cache_info(self):
        """Return the cache information"""
        return self.cache_data, self.frequencies
