from flask import Flask
import pytest

@pytest.fixture
def app():
    app=Flask(__name__)
    return app

@pytest.fixture
def client(app):
    return app.test_client()