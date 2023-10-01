#!/usr/bin/env python3
"""script async """
import asyncio
from typing import List
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Execute async_comprehension 4 times in parallel using asynciogather"""
    start_time = time.time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = time.time()
    total_time = end_time - start_time
