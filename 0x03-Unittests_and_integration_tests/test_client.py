#!/usr/bin/env python3
"""A github org client test
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class"""
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name, mock_get_json):
        """Test that GithubOrgClient.org returns the correct value"""
        test_class = GithubOrgClient(org_name)
        test_class.org()
        mock_get_json.assert_called_once_with(
            f'https://api.github.com/orgs/{org_name}'
        )

    def test_public_repos_url(self):
        """Test that the result of _public_repos_url is the expected one
        based on the mocked payload
        """
        with patch(
            'client.GithubOrgClient.org',
            new_callable=PropertyMock,
            return_value={"repos_url": "http://some_url.com"}
        ) as mock_org:
            test_class = GithubOrgClient("test")
            self.assertEqual(test_class._public_repos_url,
                             mock_org.return_value["repos_url"])
            mock_org.assert_called_once_with()
