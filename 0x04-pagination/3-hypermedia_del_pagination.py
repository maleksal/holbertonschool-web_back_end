#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """ Return a dictionary.
        """
        assert type(index) is int and type(page_size) is int
        assert 0 <= index < len(self.indexed_dataset())

        idxset = self.__indexed_dataset
        d = self.__dataset
        res = []
        [
            res.append((i, idxset[i])) for i in range(index, len(d))
            if i in idxset and len(res) < page_size
        ]
        return {
            'index': index,
            'data': [_[1] for _ in res],
            'page_size': len(res),
            'next_index': max([_[0] for _ in res]) + 1
        }
