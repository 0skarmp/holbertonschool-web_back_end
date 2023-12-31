#!/usr/bin/env python3
"""script python async"""
import asyncio
wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''
    printing the correct output of the wait_n coroutine
    '''
    return(asyncio.create_task(wait_random(max_delay)))
