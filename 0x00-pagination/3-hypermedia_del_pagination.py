#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names."""
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset."""
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0."""
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Returns a dict with deletion-resilient pagination."""
        assert index is not None and 0 <= index < len(self.indexed_dataset())

        indexed_data = self.indexed_dataset()
        data_keys = sorted(indexed_data.keys())
        start_index = data_keys.index(index)
        data_page = []

        # Collect data for the page
        for i in range(page_size):
            if start_index + i < len(data_keys):
                data_page.append(indexed_data[data_keys[start_index + i]])
            else:
                break

        next_index = data_keys[start_index + page_size]
        if start_index + page_size < len(data_keys) else None

        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data_page),
            "data": data_page,
        }
