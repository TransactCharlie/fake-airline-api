__author__ = 'Charlie'
#Builds the database and runs some tests.

import json
import unittest
import fake_airline_api
from data_lodaer import db_init
import config

TEST_DATA_FILENAME = "integration_test_data.csv"


class DBBuildTests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        db_init(TEST_DATA_FILENAME, debug = False)



    def setUp(self):
        self.app = fake_airline_api.app.test_client()



    def test_all_routes(self):
        expected = [
            {
                "Price": 100,
                "ToIATA": "LHR",
                "ReturnDate": "2014-04-07",
                "DepartureDate": "2014-04-01",
                "FromIATA": "EDI"
            },
            {
                "Price": 5000,
                "ToIATA": "EWR",
                "ReturnDate": "2014-08-12",
                "DepartureDate": "2014-08-04",
                "FromIATA": "GLA"
            }
        ]
        actual = json.loads(self.app.get('/all_routes').data)

        self.assertEqual(actual, expected)



    def test_api(self):
     expected = [
            {
                "Price": 100,
                "ToIATA": "LHR",
                "ReturnDate": "2014-04-07",
                "DepartureDate": "2014-04-01",
                "FromIATA": "EDI"
            }]
     actual = json.loads(self.app.get('/api/EDI/LHR/2014-04-01/2014-04-07').data)

     self.assertEqual(actual, expected)