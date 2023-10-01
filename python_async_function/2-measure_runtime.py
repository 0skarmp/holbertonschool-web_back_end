#!/usr/bin/env python3
"""scritp asycn"""
import asyncio
import time
wait_n = __import__("1-concurrent_coroutines.py").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """function to measure the average execution time of wait_n"""
    time1 = time.time()
    asyncio.run(wait_n(n, max_delay))
    time0 = time.time()
    total_time = time1 - time0
    return total_time / n
