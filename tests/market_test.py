# import pytest
# import requests
# from flask import jsonify
# from requests.exceptions import ConnectionError
# class TestApi(unittest.TestCase):
#     GET_URL = 'https://api.bittrex.com/api/v1.1/public/getmarketsummaries'
#     POST_URL = 'https://api.bittrex.com/api/v1.1/public/getmarketsummary?market=btc-ltc'
#
#     def test_get_market(self):
#         try:
#             resp = requests.get(self.GET_URL)
#             self.assertEqual(resp.status_code,200)
#             print("test1 is completed")
#         except requests.exceptions.ConnectionError as r:
#             return jsonify("Error occurred => ", str(r))
#
#     def test_post_market(self):
#         try:
#             resp = requests.post(self.POST_URL)
#             self.assertEqual(resp.status_code,200)
#             print("test2 is completed")
#         except requests.exceptions.ConnectionError as r:
#             return jsonify("Error occurred => ", str(r))
#
# if __name__ == "__main__":
#     tester = TestApi()
#     tester.test_get_market()
#     unittest.main()

#

from flask import url_for
import json
from Crypto_currency_market_updates.settings import AUTH_TOKEN
from requests.exceptions import HTTPError,InvalidHeader,MissingSchema,InvalidSchema

class TestCases:
    def test_valid_market_data(self, client):
        """
        :Summary: This test case for checking user provided valid authentication or token
        """
        try:
            auth_token = AUTH_TOKEN
            hed = {'Authorization': 'Bearer ' + auth_token}
            response = client.get(url_for('market_apis.market_summary'),headers=hed)
            assert response.status_code == 200
        except HTTPError as http_err:
            print(f'HTTP error occurred: {http_err}')

    def test_invalid_market_data(self, client):
        """
        :Summary: This test case for checking if user not provided valid authentication or token
        """
        try:
            response = client.get(url_for('market_apis.market_summary'))
            assert response.status_code == 400
            assert json.loads(response.data)['message'] == 'Please provide valid token'
        except InvalidHeader as error:
            print(f'Invalid Header error occurred: {error}')

    def test_valid_market_details_missing_params(self, client):
        """
        :Summary: This test case for checking if user not provided market_details inside params.
        """
        try:
            auth_token = AUTH_TOKEN
            hed = {'Authorization': 'Bearer ' + auth_token}
            response = client.get(url_for('market_apis.market_summary'),headers=hed)
            assert response.status_code == 400
            assert json.loads(response.data)['message'] == 'Kindly provide valid market details'
        except MissingSchema as error:
            print(f'Missing params error occurred: {error}')

    def test_valid_market_details_invalid_params(self, client):
        """
        :Summary: This test case for checking if user provided invalid market_details inside params.
        """
        try:
            params = {'market': 'abc'}
            auth_token = AUTH_TOKEN
            hed = {'Authorization': 'Bearer ' + auth_token}
            response = client.post(url_for('market_apis.market_summary'), headers=hed, query_string=params)
            assert response.status_code == 400
            assert json.loads(response.data)['message'] == 'Kindly check you are provided invalid market details'
        except InvalidSchema as error:
            print(f'Invalid params error occurred: {error}')