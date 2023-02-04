#!/usr/bin/env python3
''' Test suite for various cases
'''
import unittest
from parameterized import parameterized, parameterized_class
from fixtures import TEST_PAYLOAD
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


@parameterized_class(
        ("org_payload", "repos_payload", "expected_repos", "apache2_repos"),
        TEST_PAYLOAD
)
class TestIntegrationGithubOrgClient(unittest.TestCase):
    '''Integration tests for external requests
    '''
    @classmethod
    def setUpClass(cls) -> None:
        '''called to start up the test case
        '''
        config = {'return_value.json.side_effect':
                  [
                      cls.org_payload, cls.repos_payload,
                      cls.org_payload, cls.repos_payload
                  ]
                  }
        cls.get_patcher = patch('requests.get', **config)

        cls.mock = cls.get_patcher.start()

    def test_public_repos(self):
        """ Integration test for public repos method"""
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.org, self.org_payload)
        self.assertEqual(test_class.repos_payload, self.repos_payload)
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_with_license(self):
        """ Integration test for public repos with a License """
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("XLICENSE"), [])
        self.assertEqual(test_class.public_repos(
            "apache-2.0"), self.apache2_repos)
        self.mock.assert_called()

    @classmethod
    def tearDownClass(cls):
        """Runs once tests are done"""
        cls.get_patcher.stop()
