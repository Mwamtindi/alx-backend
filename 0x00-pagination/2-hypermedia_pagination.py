#!/usr/bin/env python3
"""
This module provides hypermedia pagination functionality using `Server` class
to paginate db of popular baby names.
"""

import csv
from typing import List, Tuple, Dict
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for the page and page size.

    Args:
        page : The page number (1-indexed).
        page_size : The number of items per page.

    Returns:
        Tuple: A tuple containing the start index and end index
        for the items on the specified page.
    """
    return (page - 1) * page_size, page * page_size


class Server:
    """Server class to paginate db of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset.

        Returns:
            List[List]: The dataset of popular baby names.
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get page of dataset corresponding to page and page size.

        Args:
            page : The page number (1-indexed).
            page_size : The number of items per page.

        Returns:
            List: The requested page of items from
            the dataset, or an empty list if out of range.
        """
        assert isinstance(page, int) and page > 0, \
            "Page must be an integer greater than 0."
        assert isinstance(page_size, int) and page_size > 0, \
            "Page size must be an integer greater than 0."

        start_idx, end_idx = index_range(page, page_size)
        dataset = self.dataset()

        if start_idx >= len(dataset):
            return []

        return dataset[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Get a hypermedia pagination dict for the dataset.

        Args:
            page : The page number (1-indexed).
            page_size : The number of items per page.

        Returns:
            Dict: A dict with pagination information.
        """
        data = self.get_page(page, page_size)
        total_items = len(self.dataset())
        total_pages = math.ceil(total_items / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
