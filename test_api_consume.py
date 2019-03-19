#test_api_consume.py

import unittest
from mock import Mock, patch
from api_consume import api_get, api_count

class ApiTest(unittest.TestCase):


    def setUp(self):
        pass

    @patch('api_consume.requests.get')
    def test_api_can_respond(self,  mock_get):
        mock_get.return_value.ok  = True
        response = api_get()
        self.assertIsNotNone(response)

    @patch('api_consume.api_count')
    def test_api_can_count_first_10(self, mock_count):
        mock_count = 5
        self.assertGreater(mock_count, 4)


if __name__ == '__main__':
    unittest.main()