from flask import url_for
import json
from Crypto_currency_market_updates.settings import AUTH_TOKEN
from requests.exceptions import HTTPError,InvalidHeader,MissingSchema,InvalidSchema

class TestMarketData:
    def test_valid_market_data(self, client):
        """
        :Summary: This test case for checking user provided valid authentication or token
        """
        try:
            auth_token = AUTH_TOKEN
            headers = {'Authorization': 'Bearer ' + auth_token}
            response = client.get(url_for('market_apis.market_summary'),headers=headers)
            assert json.loads(response.data)['success'] == True
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
            headers = {'Authorization': 'Bearer ' + auth_token}
            response = client.get(url_for('market_apis.market_summary'),headers=headers)
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
            headers = {'Authorization': 'Bearer ' + auth_token}
            response = client.post(url_for('market_apis.market_summary'), headers=headers, query_string=params)
            assert response.status_code == 400
            assert json.loads(response.data)['message'] == 'Kindly check you are provided invalid market details'
        except InvalidSchema as error:
            print(f'Invalid params error occurred: {error}')