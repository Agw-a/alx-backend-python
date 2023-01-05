#!/usr/bin/env bash

'''Defines task 9 module
'''

from typing import Iterable, List, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''length of a list
    '''
    return [(i, len(i)) for i in lst]
