import logging
from flask import request,jsonify,Blueprint
from datetime import datetime
from flask_restful import Resource,Api
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

# For structurize flask application
auth_apis = Blueprint('auth_apis',__name__)
api=Api(auth_apis)

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
			email = request.json.get('email', None)
			password = request.json.get('password', None)
			mobile_number = request.json.get('mobile_number', None)
			user = User(email=email,password=password,mobile_number=mobile_number)
			user.hash_password()   # Hashing the password
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
		:summary:-> This API will use for user Login to generate the JWT token.
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
			email = request.json.get('email',None)
			password = request.json.get('password',None)
			user = User.objects.get(email=email)
			authorized = user.check_password(password=password) # checking user password from DB
			if not authorized:
				return {'error': 'Email or password invalid'}, 401
			expires = datetime.timedelta(days=30)
			access_token = create_access_token(identity=str(user.id), expires_delta=expires)
			return {"result":"User Logged in Successfully","success":True,'token': access_token}, 200
		except (UnauthorizedError, DoesNotExist) as error:
			logger.error("Error occurred => ", str(error))
			raise UnauthorizedError
		except Exception as error:
			logger.error("Error occurred => ", str(error))
			raise InternalServerError

api.add_resource(Signup_Api,"/user_signup")
api.add_resource(Login_Api,"/user_Login")