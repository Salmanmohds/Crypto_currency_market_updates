from flask_bcrypt import generate_password_hash,check_password_hash
from .db import db


class User(db.Document):
 email = db.EmailField(required=True, unique=True)
 password = db.StringField(required=True, min_length=6)
 mobile_number = db.StringField(required=True, min_length=10)


 # This function used for Hash the password
 def hash_password(self):
  self.password = generate_password_hash(self.password).decode('utf8') # For converting Bytes data to string object.
  print(self.password)

 # This function used for check the password
 def check_password(self, password):
  return check_password_hash(self.password, password)