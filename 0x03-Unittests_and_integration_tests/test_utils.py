#!/usr/bin/env python3
''' Test suite for various cases
'''
import unittest
from unittest.mock import patch, Mock
from parameterized import parameterized
from utils import access_nested_map, get_json
from typing import Mapping, Sequence, Any, Dict


class TestAccessNestedMap(unittest.TestCase):
    '''Tests nested map'''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"),  2)
    ])
    def test_access_nested_map(
            self, nested_map: Mapping,
            path: Sequence,
            result: Any) -> None:
        ''' Test return value of utils.access_nested_map() '''
        self.assertEqual(access_nested_map(nested_map, path), result)

    @parameterized.expand([
        ({}, ("a",), KeyError),
        ({"a": 1}, ("a", "b"), KeyError)
    ])
    def test_access_nested_map_exception(
            self, nested_map: Mapping,
            path: Sequence,
            key: Exception) -> None:
        '''Tests exception raised by utils.access_nested_map'''
        with self.assertRaises(key):
            access_nested_map(nested_map, path)


class TestGetJson(unittest.TestCase):
    """Tests get_json function
    """
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False})
    ])
    def test_get_json(self,
                      test_url: str,
                      test_payload: Dict) -> None:
        '''test that utils.get_json returns the expected result.
        '''
        #  Patch requests.get
        test_configuration = {"return_value.json.return_value": test_payload}
        patches = patch("requests.get", **test_configuration)
        mock = patches.start()
        self.assertEqual(get_json(test_url), test_payload)
        mock.assert_called_once()
        patches.stop()
