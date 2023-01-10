#!/usr/bin/env python3

'''Module that measures task execution time
'''
import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''Measures task time
    '''
    begn = time.perf_counter()
    task = [async_comprehension() for i in range(4)]
    await asyncio.gather(*task)
    end_t = time.perf_counter()
    return (end_t - begn)
