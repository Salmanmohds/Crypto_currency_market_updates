# from flask import Flask,jsonify,Response,make_response
# from flask_bcrypt import Bcrypt
# from flask_restful import Resource,Api
# import requests
# from .config.config import market_summary_url, market_access_url,JWT_SECRET_KEY
# import logging
# import json
# from flask_mongoengine import MongoEngine
# from flask_jwt_extended import jwt_required, JWTManager
# from decouple import config
# from flask_jwt_extended.exceptions import NoAuthorizationError,JWTExtendedException
# from .errors import InternalServerError,UnauthorizedError,UnauthorizedTokenError,SchemaValidationError,EmailAlreadyExistsError
# from .errors import errors
#
# # logger configuration
# logger = logging.getLogger(__name__)
# logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
#                     datefmt='%H:%M:%S',
#                     level=logging.DEBUG)
#
# app = Flask(__name__)
# api = Api(app, errors=errors)
# bcrypt = Bcrypt(app)
# # MongoDB configuration
# app.config['MONGODB_SETTINGS'] = {
#     'db': 'User12',
#     'host': 'localhost',
#     'port': 27017
# }
# db = MongoEngine()
# db.init_app(app)
#
# # SetUp the Flask JWT Extended extension
# jwt = JWTManager(app)
# app.config["JWT_SECRET_KEY"] = "super-secret"
#
#
# class Market_Summary(Resource):
# 	@jwt_required()
# 	def get(self):
# 		"""
# 		:summary:-> This api used for return all market summary updates
# 		# Todo-> Need to check exception later
# 		"""
# 		try:
# 			response = requests.get(url=market_summary_url).json()
# 			return Response(response=json.dumps({"data": {"result": response}}),status=200,mimetype="application/json")
# 		except (NoAuthorizationError,JWTExtendedException) as error:
# 			app.logger.error("Invalid token => ", str(error))
# 			raise UnauthorizedTokenError
# 		except Exception as error:
# 			app.logger.error(f"Error occurred: {str(error)}")
# 			raise InternalServerError
#
# 	@jwt_required()
# 	def post(self):
# 		"""
# 		:summary:-> This API will return of a specific market details.
# 		:param:-> {
# 					market = btc-ltc
# 				  }
# 		:return:
# 				{
# 				"data": {
# 					"result": {
# 						"success": true,
# 						"message": "",
# 						"result": [
# 							{
# 								"MarketName": "BTC-LTC",
# 								"High": 0.0028214,
# 								"Low": 0.00249626,
# 								"Volume": 6281.87390068,
# 								"Last": 0.00250588,
# 								"BaseVolume": 16.00782485,
# 								"TimeStamp": "2022-03-02T16:32:08.12",
# 								"Bid": 0.00250285,
# 								"Ask": 0.00250498,
# 								"OpenBuyOrders": 299,
# 								"OpenSellOrders": 3243,
# 								"PrevDay": 0.002565,
# 								"Created": "2014-02-13T00:00:00"
# 							}
# 						]
# 					}
# 				}
# 			}
# 		"""
# 		# Todo-> Need to check exception and some validation as per requirement later
# 		try:
# 			market_params  = request.args.get('market','') or None
# 			response = requests.post(url=market_access_url,params={"market":market_params}).json()
# 			return Response(response=json.dumps({"data": {"result": response}}), status=200, mimetype="application/json")
# 		except (NoAuthorizationError,JWTExtendedException) as error:
# 			app.logger.error("Invalid token => ", str(error))
# 			raise UnauthorizedTokenError
# 		except Exception as error:
# 			app.logger.error(f"Error occurred: {str(error)}")
# 			raise InternalServerError
#
#
# # Todo-> Need to be divide API or structure using Blueprint or any other way
#
# from flask import request
# from datetime import datetime,timedelta
# from flask_restful import Resource,Api
# from .model import User
# import datetime
# from flask_jwt_extended import create_access_token,create_refresh_token,get_jwt_identity
# from mongoengine.errors import FieldDoesNotExist,NotUniqueError,DoesNotExist,ValidationError,InvalidQueryError
#
# # Todo: Need to be check exception later
# class Signup_Api(Resource):
# 	def post(self):
# 		try:
# 			body = request.get_json()
# 			user = User(**body)
# 			user.hash_password()
# 			user.save()
# 			id = user.id
# 			return jsonify({"result":"User Signup Successfully"})
# 		except FieldDoesNotExist:
# 			raise SchemaValidationError
# 		except NotUniqueError:
# 			raise EmailAlreadyExistsError
# 		except Exception as e:
# 			raise InternalServerError
#
# # Todo: Need to be check exception later
# class Login_Api(Resource):
# 	def post(self):
# 		try:
# 			body = request.get_json()
# 			user = User.objects.get(email=body.get('email'))
# 			authorized = user.check_password(body.get('password'))
# 			if not authorized:
# 				return {'error': 'Email or password invalid'}, 401
# 			expires = datetime.timedelta(days=7)
# 			access_token = create_access_token(identity=str(user.id), expires_delta=expires)
# 			return {'token': access_token}, 200
# 		except (UnauthorizedError, DoesNotExist):
# 			raise UnauthorizedError
# 		except Exception as error:
# 			logger.error("Error occurred => ", str(error))
# 			raise InternalServerError
#
#
# # Todo:-> Need to be bifurcate later
# api.add_resource(Signup_Api,'/user_signup')
# api.add_resource(Login_Api,'/user_Login')
# api.add_resource(Market_Summary,'/market-data')
#
# if __name__ == '__main__':
# 	app.run(debug=True)

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
# from .database.db import initialize_db
from database.db import initialize_db
from flask_restful import Api
from view.routes import initialize_routes
from view.errors import errors
from flask_swagger_ui import get_swaggerui_blueprint
app = Flask(__name__)
api = Api(app, errors=errors)
bcrypt = Bcrypt(app)
jwt = JWTManager(app)

# Swagger configuration
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Seans-Python-Flask-REST-Boilerplate"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
# MongoDB configuration
# Todo:-> Need to check while using docker compose
app.config['MONGODB_SETTINGS'] = {
    'host': 'mongodb://localhost/User12'
}

# Todo:-> Need to define inside .env file later
# JWT configuration
app.config["JWT_SECRET_KEY"] = "super-secret"

initialize_db(app)
initialize_routes(api)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')