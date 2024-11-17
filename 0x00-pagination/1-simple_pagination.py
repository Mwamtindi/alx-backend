#!/usr/bin/env python3
"""
This module provides pagination functionality using `Server` class to paginate
a database of popular baby names.
"""

import csv
from typing import List, Tuple
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end idx for the page and page size.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple: A tuple containing the start idx and end idx
        for the items on the specified page.
    """
    """start_indx = (page - 1) * page_size
    end_indx = start_indx + page_size
    return start_indx, end_indx"""
    return ((page - 1) * page_size, page * page_size)


class Server:
    """Server class to paginate a db of popular baby names."""
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
        Get a page of the dataset corresponding to the page and page size.

        Args:
            page (int): The page number (1-indexed).
            page_size (int): The number of items per page.

        Returns:
            List[List]: The requested page of items from
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
