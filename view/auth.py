import logging
from flask import request,jsonify
from datetime import datetime
from flask_restful import Resource
import datetime
from flask_jwt_extended import create_access_token
from mongoengine.errors import FieldDoesNotExist,NotUniqueError,DoesNotExist
from .errors import InternalServerError,UnauthorizedError,SchemaValidationError,EmailAlreadyExistsError
from Crypto_currency_market_updates.database.model import User


# logger configuration
logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)


class Signup_Api(Resource):
	def post(self):
		"""
		:summary:-> This API will use for user Signup. The data will store in the MongoDB.
		:request: {
					email: salman.m@gmail.com
					password: salman123
					mobile_number: 5874845784
					}
		:return:
			{
    		  "result": "User Signup Successfully"
			}
		"""
		try:
			body = request.get_json()
			user = User(**body)
			user.hash_password()
			user.save()
			return jsonify({"result":"User Signup Successfully"})
		except FieldDoesNotExist as error:
			logger.error("Error occurred => ", str(error))
			raise SchemaValidationError
		except NotUniqueError as error:
			logger.error("Error occurred => ", str(error))
			raise EmailAlreadyExistsError
		except Exception as error:
			logger.error("Error occurred => ", str(error))
			raise InternalServerError


class Login_Api(Resource):
	def post(self):
		"""
		:summary:-> This API will use for user Login.
		:request: {
					email: salman.m@gmail.com
					password: salman123
				  }
		:return:
				{
		    	  "token": User will get JWT-Token for accessing to our main Market Api
				}
		"""
		try:
			body = request.get_json()
			user = User.objects.get(email=body.get('email'))
			authorized = user.check_password(body.get('password'))
			if not authorized:
				return {'error': 'Email or password invalid'}, 401
			expires = datetime.timedelta(days=7)
			access_token = create_access_token(identity=str(user.id), expires_delta=expires)
			return {'token': access_token}, 200
		except (UnauthorizedError, DoesNotExist) as error:
			logger.error("Error occurred => ", str(error))
			raise UnauthorizedError
		except Exception as error:
			logger.error("Error occurred => ", str(error))
			raise InternalServerError
