#!/usr/bin/evn python3
"""scritp asycn python"""
import asyncio
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """Get 10 random numbers using an async comprehension over async_generator
    Returns a list of the 10 random numbers"""
    random_numbers = [result async for result in async_generator()]
    return random_numbers
