#!/usr/bin/env python3

'''Async compresion module
'''
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''Returns list generated by astnc_generator
    '''
    n = async_generator()
    return [i async for i in n]
