#!/usr/bin/env python3
""" MRUCaching with caching machine """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """MRUCache is a caching system that uses the MRU eviction policy."""

    def __init__(self):
        """Initialize MRUCache by calling parent initializer"""
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """Add an item to the cache using MRU policy if limit is reached """
        if key and item:
            if key in self.cache_data:
                self.cache_data[key] = item
                return
            elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                discard = self.queue.pop()
                del self.cache_data[discard]
                print("DISCARD:", discard)
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve item from cache by key and mark it as recently used"""
        if key in self.cache_data:
            self.queue.remove(key)
            self.queue.append(key)
            return self.cache_data[key]
        return None
