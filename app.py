from flask import Flask,jsonify,Response,make_response
from flask_restful import Resource,Api
import requests
from .constants.http_status_codes import ERROR_TECHNICAL,ERROR_BAD_REQUEST
from .config.config import market_summary_url, market_access_url
import logging
import json
from flask import request
logger = logging.getLogger(__name__)

logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

app = Flask(__name__)
api = Api(app)

class Market_Summary(Resource):
	def get(self):
		"""
		:summary:-> This api for return all market summary
		"""
		try:
			response = requests.get(url=market_summary_url).json()
			return Response(response=json.dumps({"data": {"result": response}}),status=200,mimetype="application/json")
		except Exception as error:
			app.logger.error(f"Error occurred: {str(error)}")
			return Response(response=json.dumps({"message": ERROR_BAD_REQUEST, "status": 400}), status=400)

	def post(self):
		"""
		:summary:-> This API will return of a specific market details.
		:param:-> {market = btc-ltc}
		:return:
				{
				"data": {
					"result": {
						"success": true,
						"message": "",
						"result": [
							{
								"MarketName": "BTC-LTC",
								"High": 0.0028214,
								"Low": 0.00249626,
								"Volume": 6281.87390068,
								"Last": 0.00250588,
								"BaseVolume": 16.00782485,
								"TimeStamp": "2022-03-02T16:32:08.12",
								"Bid": 0.00250285,
								"Ask": 0.00250498,
								"OpenBuyOrders": 299,
								"OpenSellOrders": 3243,
								"PrevDay": 0.002565,
								"Created": "2014-02-13T00:00:00"
							}
						]
					}
				}
			}
		"""
		try:
			market_params  = request.args.get('market','') or None
			response = requests.post(url=market_access_url,params={"market":market_params}).json()
			return Response(response=json.dumps({"data": {"result": response}}), status=200, mimetype="application/json")
		except Exception as error:
			app.logger.error(f"Error occurred: {str(error)}")
			return Response(response=json.dumps({"message": ERROR_BAD_REQUEST, "status": 400}), status=400)



api.add_resource(Market_Summary,'/market-data')

if __name__ == '__main__':
	app.run(debug=True)

