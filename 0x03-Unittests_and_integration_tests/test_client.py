#!/usr/bin/env python3
''' Test suite for various cases
'''
import unittest
from parameterized import parameterized
from unittest.mock import patch, PropertyMock
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    '''implements the test_org method.
    '''
    @parameterized.expand([
        ('google'),
        ('abc')
    ])
    @patch('client.get_json')
    def test_org(self, test_input, mock_config):
        ''' test that GithubOrgClient.org returns the correct value.
        '''
        test_class = GithubOrgClient(test_input)
        test_class.org()
        test_url = f'https://api.github.com/orgs/{test_input}'
        mock_config.assert_called_once_with(test_url)

    def test_public_repos_url(self):
        '''Tests that public_repos_url returns expected results
        '''
        with patch(
                'client.GithubOrgClient.org',
                new_callable=PropertyMock
                )as mock_client:
            load_url = {"repos_url": ""}
            mock_client.return_value = load_url
            test_class = GithubOrgClient("google")
            output = test_class._public_repos_url
            self.assertEqual(output, load_url['repos_url'])

    @patch('client.get_json')
    def test_public_repos(self, json):
        '''unit-test GithubOrgClient.public_repos
        '''
        json_load = [{"name": "abc"}, {"name": "vercel"}]
        json.return_value = json_load
        with patch('client.GithubOrgClient._public_repos_url',
                   new_callable=PropertyMock) as mock:
            mock.return_value = "hello/world"
            test_class = GithubOrgClient('test')
            res = test_class.public_repos()

            query = [i['name'] for i in json_load]
            self.assertEqual(res, query)

            mock.assert_called_once()
            mock.assert_called_once()
