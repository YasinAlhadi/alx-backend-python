#!/usr/bin/env python3
"""A github org client test
"""
import unittest
from unittest.mock import patch, PropertyMock
from parameterized import parameterized
from client import GithubOrgClient
from fixtures import TEST_PAYLOAD
from typing import (
    List,
    Dict,
)


class TestGithubOrgClient(unittest.TestCase):
    """TestGithubOrgClient class"""
    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json')
    def test_org(self, org_name: str, mock_get_json):
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

    @patch('client.get_json')
    def test_public_repos(self, mock_get_json):
        """Test that the list of repos is what you expect from the chosen
        payload
        """
        payload = [{"name": "Google"}, {"name": "Twitter"}]
        mock_get_json.return_value = payload
        with patch(
            'client.GithubOrgClient._public_repos_url',
            new_callable=PropertyMock,
            return_value="test_url"
        ) as mock_public_repos_url:
            test_class = GithubOrgClient("test")
            repos = test_class.public_repos()
            self.assertEqual(repos, ["Google", "Twitter"])
            mock_get_json.assert_called_once_with("test_url")
            mock_public_repos_url.assert_called_once_with()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test has_license method"""
        test_class = GithubOrgClient("test")
        self.assertEqual(
            test_class.has_license(repo, license_key),
            expected
        )
