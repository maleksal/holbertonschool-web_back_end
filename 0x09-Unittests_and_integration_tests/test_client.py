#!/usr/bin/env python3
""" test client module """

from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest.mock import patch


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class for client.GithubOrgClient."""

    @parameterized.expand([
        ("google", {}),
        ("abc", {})
        ])
    @patch("client.get_json")
    def test_org(self, url, result, mock):
        """test GithubOrgClient.org if it returns the correct value."""

        mock.return_value = {}

        a_class = GithubOrgClient(url)

        self.assertEqual(a_class.org, result)

        mock.assert_called_once()


if __name__ == '__main__':
    unittest.main()
