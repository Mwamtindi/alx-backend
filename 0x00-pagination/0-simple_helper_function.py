#!/usr/bin/env python3
"""
This module contains the func `index_range` for pagination purposes.
"""

from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Calculate the start and end index for the given page and page size.

    Args:
        page (int): The page number (1-indexed).
        page_size (int): The number of items per page.

    Returns:
        Tuple: Tuple containing start idx ,end idx for items on specified page.
    """
    start_indx = (page - 1) * page_size
    end_indx = start_indx + page_size
    return start_indx, end_indx
