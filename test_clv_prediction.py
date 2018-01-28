import unittest
import api
import json
import sys


class TestFlaskApi(unittest.TestCase):
    def setUp(self):
        self.app = api.app.test_client()

    def test_hello_world(self):
        response = self.app.get('/')
        self.assertEqual(json.loads(response.get_data().decode(sys.getdefaultencoding())), {'hello': 'world'})

    def test_get_prediction(self):
        response = self.app.get('/customers/0001b3166c1bcb11f331e6676f7863a9')
        data = json.loads(response.get_data())
        self.assertAlmostEqual(data['predicted_clv'], 113.28534850355344, places=14)


if __name__ == "__main__":
    unittest.main()