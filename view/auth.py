from flask import Flask,jsonify,Response,make_response
import logging
from flask import request
from datetime import datetime
from flask_restful import Resource,Api
import datetime
from flask_jwt_extended import create_access_token,create_refresh_token,get_jwt_identity
from mongoengine.errors import FieldDoesNotExist,NotUniqueError,DoesNotExist,ValidationError,InvalidQueryError
from .errors import InternalServerError,UnauthorizedError,UnauthorizedTokenError,SchemaValidationError,EmailAlreadyExistsError
from database.model import User

# logger configuration
logger = logging.getLogger(__name__)
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)

# Todo: Need to be check exception later
class Signup_Api(Resource):
	def post(self):
		try:
			body = request.get_json()
			user = User(**body)
			user.hash_password()
			user.save()
			id = user.id
			return jsonify({"result":"User Signup Successfully"})
		except FieldDoesNotExist:
			raise SchemaValidationError
		except NotUniqueError:
			raise EmailAlreadyExistsError
		except Exception as e:
			raise InternalServerError

# Todo: Need to be check exception later
class Login_Api(Resource):
	def post(self):
		try:
			body = request.get_json()
			user = User.objects.get(email=body.get('email'))
			authorized = user.check_password(body.get('password'))
			if not authorized:
				return {'error': 'Email or password invalid'}, 401
			expires = datetime.timedelta(days=7)
			access_token = create_access_token(identity=str(user.id), expires_delta=expires)
			return {'token': access_token}, 200
		except (UnauthorizedError, DoesNotExist):
			raise UnauthorizedError
		except Exception as error:
			logger.error("Error occurred => ", str(error))
			raise InternalServerError