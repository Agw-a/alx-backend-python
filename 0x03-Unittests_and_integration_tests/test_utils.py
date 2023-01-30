#!/usr/bin/env python3
''' Test suite for various cases
'''
import unittest
from parameterized import parameterized, parameterized_class, param
from utils import access_nested_map
from typing import Mapping, Sequence, Any


class TestAccessNestedMap(unittest.TestCase):
    @parameterized.expand([
        ({"a": 1},("a",), 1),
        ({"a": {"b": 2}},("a",), {"b": 2}),
        ({"a": {"b": 2}},("a", "b"),  2)
    ])
    def test_access_nested_map(self, nested_map: Mapping, path: Sequence, result: Any) -> None:
        ''' Test return value of utils.access_nested_map() '''
        self.assertEqual(access_nested_map(nested_map, path), result)
