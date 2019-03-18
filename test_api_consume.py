import unittest
from api_consume import api_get, api_count

class ApiTest(unittest.TestCase):

    def setUp(self):
        self.request = api_get('https://jsonplaceholder.typicode.com/todos')

    def test_api_can_respond(self):
        respond = self.request.status_code
        self.assertEqual(respond, 200)
    
    def test_api_can_count_first_10(self):
        totalrecords = api_count(self.request.content)
        self.assertGreater(totalrecords, 5)


if __name__ == '__main__':
    unittest.main()