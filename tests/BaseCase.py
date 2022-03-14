import unittest
from app import app
from database.db import db

class BaseCase(unittest.TestCase):
    """
        For set up the environment and check the health connection
    """
    def setUp(self):
        self.app = app.test_client()
        self.db = db.get_db()

    def tearDown(self):
        """
            Delete Database collections after the test is complete also close all
            the connection after execution is complete.
        """
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)