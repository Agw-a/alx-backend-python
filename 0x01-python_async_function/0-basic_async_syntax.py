#!/usr/bin/env python3

'''Task 0
'''
import asyncio
import random

'''
takes an argument and returns based on range
'''


async def wait_random(max_delay: int = 10) -> float:
    '''
    defines a coroutine
    '''
    i = random.uniform(0, max_delay)
    await asyncio.sleep(i)
    return i
