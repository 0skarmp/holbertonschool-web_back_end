#!/usr/bin/env python3
"""async functions """
import asyncio
import random


async def asynchronus(max_delay: int = 10) -> float:
    """Asynchronous function that generates a random
        float and sleeps for a random
        duration before returning the generated float."""
    float and sleeps for a randon
    duration before returning the generated float.
    aleatory = random.uniform(0, max_delay)
    await asyncio.sleep(aleatory)
    return aleatory
