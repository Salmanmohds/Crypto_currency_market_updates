from flask_mongoengine import MongoEngine

db = MongoEngine()
# This function used for connect with MongoDB
def initialize_db(app):
    db.init_app(app)