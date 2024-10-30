#!/usr/bin/env python3
""" BasicCache module with a caching system.
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """BasicCache inherits from BCa and is caching syst with no limit."""

    def put(self, key, item):
        """Assign item to cache_data dict using provided key.

        Args:
            key: The key to be assigned in the cache.
            item: The item to store in the cache.
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """Retrieve item from cache_data dictionary using the key.

        Args:
            key: The key associated with the item.

        Returns:
            The in cache_data,None if key is None or not in cache.
        """
        return self.cache_data.get(key, None)
