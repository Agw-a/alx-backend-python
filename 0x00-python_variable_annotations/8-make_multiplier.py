#!/usr/bin/env bash

'''takes a float and returns a function
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Create a multiplier function
    '''
    return lambda x: x * multiplier
