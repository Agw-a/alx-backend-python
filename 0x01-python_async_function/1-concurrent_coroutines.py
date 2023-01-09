#!/usr/bin/env python3
'''Task 1 module
'''

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax.py').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Execute await a number of times
    return number of delays
    '''
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    delays = [await task for task in asyncio.as_completed(tasks)]
    return delays
