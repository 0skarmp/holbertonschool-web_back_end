#!/usr/bin/env python3
"""script generates 10 times random numberes every one second"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    for n in range(10):
        yield random.uniform(0, 10)
        await asyncio.sleep(n)
