#!/usr/bin/env python3
"""
Simple pagination module.
"""

import csv
import math
from typing import Dict, List


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of size two containing a start index and an end index.
    """
    s, e = page * page_size, page * page_size
    return (s - page_size, e)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        takes two arguments page with default value 1 and page_size with 10.
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0

        # start, end indexes
        srange, erange = index_range(page, page_size)

        dataset = self.dataset()

        if srange <= len(dataset) and erange <= len(dataset):
            return dataset[srange: erange]
        return []

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """ Returns a dictionary containing the following key-value pairs.
        """
        d = self.get_page(page, page_size)
        np = None if page_size * page + 1 > len(self.__dataset) else page + 1
        result = {
            "page_size": len(d),
            "page": page,
            "data": d,
            "next_page": np,
            "prev_page": None if page == 1 else page - 1,
            "total_pages": math.ceil(len(self.__dataset) / page_size)
        }
        return result
