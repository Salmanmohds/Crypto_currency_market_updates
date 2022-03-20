import unittest
from Crypto_currency_market_updates.tests.conftest import app
from Crypto_currency_market_updates.database.db import db

class BaseCase(unittest.TestCase):
    """
        For set up the environment and check the health connection
    """
    def setUp(self):
        self.app = app.test_client()
        self.db = db.get_db()  # getting database instance

    def tearDown(self):
        """
            Delete Database collections after the test is complete also close all
            the connection after execution is complete.
        """
        for collection in self.db.list_collection_names():  # find all collection name
            self.db.drop_collection(collection)