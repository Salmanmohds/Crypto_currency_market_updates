from flask import url_for
from tests.conftest import client
import json,os


class TestScenarios:
    def test_valid_marketsummary_header(self,client):
        response = client.get(url_for('market_api.home'))
        assert response.status_code ==200
