#!/usr/bin/env python3

'''Takes a list of floats and returns sum as float
'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''return the sum of elements in a list
    '''

    sums: float = 0.0

    for i in range(0, len(input_list)):
        sums = sums + input_list[i]
    return sums
