#!/usr/bin/env python3
'''Tests
'''

import unittest
import requests
from utils import access_nested_map, get_json, memoize
from parameterized import parameterized
from unittest import mock
from unittest.mock import patch


class TestAccessNestedMap(unittest.TestCase):
    '''
    Class that inherits from unittest.TestCase
    '''
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, returned):
        '''
        tests that the method returns.
        '''
        self.assertEqual(access_nested_map(nested_map, path), returned)

    @parameterized.expand([
        ({}, ('a')),
        ({'a': 1}, ('a', 'b'))
        ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test that a KeyError is raised """
        self.assertRaises(KeyError, access_nested_map, nested_map, path)


class TestGetJson(unittest.TestCase):
    """Class TestGetJson"""

    @parameterized.expand([
        ({"test_url": "http://example.com"}, {"test_payload": True}),
        ({"test_url": "http://holberton.io"}, {"test_payload": False})
    ])
    def test_get_json(self, test_url, test_payload):
        """test that utils.get_json returns the expected result."""

        with patch('requests.get') as mock_request:

            mock_request.return_value.json.return_value = test_payload

            self.assertEqual(get_json(test_url), test_payload)

            mock_request.assert_called_once()
