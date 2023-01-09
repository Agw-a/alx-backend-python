#!/usr/bin/env python3

'''Tak 4 module
'''
import asyncio
from typing import

task_wait_n = __import__('3-tasks').task_wait_random


async def task_await_n(n: int, max_delay: int) -> List[float]:
    '''return a list of delayed tasks
    '''
    tasks = [task_wait_random(max_delay) for _ in range(n)]
    delayed_tasks = [await task for task in asyncio.as_completed(tasks)]
    return delayed_tasks
