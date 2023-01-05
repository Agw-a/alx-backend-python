#!/usr/bin/env bash

'''that takes a string k and an int OR float v and returns a tuple
'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''convert key and value to tiple of key and square
    of the value
    '''
    return (k, float(v**2))
