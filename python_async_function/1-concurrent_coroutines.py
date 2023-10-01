#!/usr/bin/env python3
"""scritp async python"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """scritp to return list of delays in ascending order"""
    many_delays = [wait_random(max_delay) for o in range(n)]
    Result = []

    for m in asyncio.as_completed(many_delays):
        result = await m
        Result.append(result)
    return Result
