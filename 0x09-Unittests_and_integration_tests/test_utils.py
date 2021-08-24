
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
