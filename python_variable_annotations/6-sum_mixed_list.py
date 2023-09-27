#!/usr/bin/env python3
"""scrip to return a float of mix int and float"""

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Sums the elements in a list of integers and floats"""
    for nums_mixed in mxd_lst:
        n_float = 0
        n_float += float(nums_mixed)
        return n_float
