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
            "repos_url": "http://google.com"
        }

        with patch.object(GithubOrgClient, "org",
                          new_callable=Property, return_value=data) as mock_o:

            G_client = GithubOrgClient(data.get("url"))

            mock_o.assert_called_once()

            self.assertEqual(
                G_client._public_repos_url,
                data.get("repos_url")
            )

    @patch("client.get_json")
    def test_public_repos(self, get_patch):
        '''
        Test list of repos is expected from payload.
        '''

        get_patch.return_value = [{"name": "google"},
                                  {"name": "abc"}]

        with patch.object(GithubOrgClient, "_public_repos_url",
                          new_callable=Property,
                          return_value="http://google.com") as mock_o:

            G_client = GithubOrgClient("facebook")

            self.assertEqual(
                G_client.public_repos(),
                ["google", "abc"]
            )

            get_patch.assert_called_once()

            mock_o.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False)
    ])
    def test_has_license(self, repo, license, expected):
        '''
        Test test_has_license method.
        '''
        G_client = GithubOrgClient("facebook")

        self.assertEqual(
            G_client.has_license(repo, license),
            expected
        )


@parameterized_class(
    ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
    TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """ example payloads anything is anything  """
    @classmethod
    def setUpClass(cls):
        """
        method to setup patcher.
        """
        cls.get_patcher, cls.mock = (

            patch('requests.get'),
            cls.get_patcher.start()

        )
        cls.mock.return_value.json.side_effect = [

            cls.org_payload, cls.repos_payload,
            cls.org_payload, cls.repos_payload,

        ]

    @classmethod
    def tearDownClass(cls):
        """method stops patcher """
        cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()
