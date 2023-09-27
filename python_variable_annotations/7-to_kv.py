#!/usr/bin/env python3
""" scrit to retunr a square and tuple of str and float"""

from typing import Tuple, Union


def to_kv(k: str, v Union[int, float]) -> Tuple(str, float):
    """Takes a string and an int or float and returns a tuple"""
    square = float(v) ** 2
    return k, square
