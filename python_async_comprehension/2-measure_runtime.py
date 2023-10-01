#!/usr/bin/env python3
"""script async """
import asyncio
from typing import List
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """Execute async_comprehension 4 times in parallel using asynciogather"""
    start = time.time()
    await asyncio.gather(*[async_comprehension(), async_comprehension(),
                           async_comprehension(), async_comprehension()])
    total_runtime = time.time() - start
    return total_runtime
