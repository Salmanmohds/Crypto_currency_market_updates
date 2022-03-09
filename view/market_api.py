from flask import Response
import requests
import logging
import json
from flask_jwt_extended import jwt_required
from flask_jwt_extended.exceptions import NoAuthorizationError,JWTExtendedException
from .errors import InternalServerError, UnauthorizedTokenError
from flask import request
from flask_restful import Resource
from settings import market_access_url,market_summary_url

logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)


class Market_Summary(Resource):
	@jwt_required()
	def get(self):
		"""
		:summary:-> This api used for return all market summary updates
		"""
		try:
			response = requests.get(url=market_summary_url).json()
			return Response(response=json.dumps({"data": {"result": response}}),status=200,mimetype="application/json")
		except (NoAuthorizationError,JWTExtendedException) as error:
			logger.error("Error occurred => ", str(error))
			raise UnauthorizedTokenError
		except Exception as error:
			logger.error(f"Error occurred: {str(error)}")
			raise InternalServerError

	@jwt_required()
	def post(self):
		"""
		:summary:-> This API will return of a specific market details.
		:param:-> {
					market = btc-ltc
				  }
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
			market_params  = request.args.get('market','')
			response = requests.post(url=market_access_url,params={"market":market_params}).json()
			return Response(response=json.dumps({"data": {"result": response}}), status=200, mimetype="application/json")
		except (NoAuthorizationError,JWTExtendedException) as error:
			logger.error("Error occurred => ", str(error))
			raise UnauthorizedTokenError
		except Exception as error:
			logger.error(f"Error occurred: {str(error)}")
			raise InternalServerError