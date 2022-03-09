import pytest
import requests
from flask import Flask
from flask import jsonify

@pytest.fixture(scope="function")
def app():
    app = Flask(__name__)
    @app.route("/market-data", methods=["GET"])
    def get_market_data():
        url = 'https://api.bittrex.com/api/v1.1/public/getmarketsummaries'
        data = requests.get(url)
        return jsonify(response=data.status_code)
    return app

def test_get_market(app):
    test_client = app.test_client()
    response = test_client.get('/market-data')
    assert response.get_json() == {"response":200}

@pytest.fixture(scope="function")
def new_app():
    new_app = Flask(__name__)
    @new_app.route("/market-data1", methods=["POST"])
    def get_market_data():
        url = 'https://api.bittrex.com/api/v1.1/public/getmarketsummary?market=btc-ltc'
        data = requests.post(url)
        return jsonify(response=data.status_code)
    return new_app

def test_post_market(new_app):
    test_client = new_app.test_client()
    response = test_client.post('/market-data1')
    assert response.get_json() == {"response": 200}

# def test_post_fail_market(new_app):
#     test_client = new_app.test_client()
#     response = test_client.post('/market-data1')
#     assert response.get_json() == {"response": 401}
