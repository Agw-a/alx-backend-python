#!/usr/bin/env python3

'''function that takes a list if int and floats and returns
    sum as float
'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''return sum of list elements
    '''

    return float(sum(mxd_lst))
