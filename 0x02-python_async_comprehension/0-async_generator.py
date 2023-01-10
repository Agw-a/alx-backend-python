#!/usr/bin/env python3

'''async generator coroutine module
'''

import asyncio
from typing import Generator
import random


async def async_generator() -> Generator[float, None, None]:
    '''Synchronosly loop throgh a value 10 times
    '''
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
