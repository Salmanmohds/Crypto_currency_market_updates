from flask import Response,Blueprint
import requests
import logging
import json
from flask_jwt_extended import jwt_required
from flask_jwt_extended.exceptions import NoAuthorizationError,JWTExtendedException
from .errors import InternalServerError, UnauthorizedTokenError
from flask import request
from flask_restful import Resource,Api
from Crypto_currency_market_updates.settings import market_access_url,market_summary_url

# logger configuration
logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

# For structurize flask application
market_apis = Blueprint('market_apis',__name__)
api = Api(market_apis)

class Market_Summary(Resource):
	@jwt_required()
	def get(self):
		"""
		:summary:-> This api used for return all market summary updates
		"""
		try:
			response = requests.get(url=market_summary_url).json() # Convert python object into json string
			return Response(response=json.dumps({"data": {"result": response},"success":True}),status=200, mimetype="application/json")
		except NoAuthorizationError as error:
			logger.error("Error occurred => ", str(error))
			raise UnauthorizedTokenError
		except Exception as error:
			logger.error(f"Error occurred: {str(error)}")
			raise UnauthorizedTokenError

	@jwt_required()
	def post(self):
		"""
		:summary:-> This API will return of a specific market details.
		"""
		try:
			market_params  = request.args.get('market','')
			response = requests.post(url=market_access_url,params={"market":market_params}).json() # Convert python object into json string
			return Response(response=json.dumps({"data": {"result": response}}), status=200, mimetype="application/json")
		except (NoAuthorizationError,JWTExtendedException) as error:
			logger.error("Error occurred => ", str(error))
			raise UnauthorizedTokenError
		except Exception as error:
			logger.error(f"Error occurred: {str(error)}")
			raise InternalServerError

api.add_resource(Market_Summary,"/market_data")