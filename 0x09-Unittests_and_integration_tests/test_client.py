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

    def test_public_repos_url(self):
        '''
        Test that the result of _public_repos_url.
        '''

        data = {
            "url": "facebook",
            "repos_url": "http://taylorswift.com"
        }

        with patch.object(GithubOrgClient, "org",
                          new_callable=Property, return_value=data) as mock_o:

            github_client = GithubOrgClient(data.get("url"))

            mock_o.assert_called_once()

            self.assertEqual(
                github_client._public_repos_url,
                data.get("repos_url")
            )


if __name__ == '__main__':
    unittest.main()
