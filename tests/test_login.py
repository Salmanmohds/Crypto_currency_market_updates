import unittest
import json

from app import app
from database.db import db

class SignupTest(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.db = db.get_db()

    def test_signup_successfully(self):
        payload = json.dumps({
            "email": "miron12@gmail.com",
            "password": "miron12"
        })

        response = self.app.post('/view/auth/user_signup', headers={"Content-Type": "application/json"}, data=payload)
        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200,response.status_code)

    def tearDown(self):
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)