#!/usr/bin/env python3
"""scritp to multply a float * float"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns function that multiplies a float by the specified multiplier"""
    def function_to_multiply(x: float) -> float:
        return: x * multiplier
    return function_to_multiply
