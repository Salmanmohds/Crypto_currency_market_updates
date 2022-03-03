from flask import Flask,jsonify,Response,make_response
from flask_restful import Resource,Api
import requests
# from .constants.http_status_codes import ERROR_TECHNICAL,ERROR_BAD_REQUEST
from .config.config import market_summary_url, market_access_url
import logging
import json
from flask import request
from flask_mongoengine import MongoEngine

logger = logging.getLogger(__name__)
# logger
logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s',
                    datefmt='%H:%M:%S',
                    level=logging.DEBUG)



app = Flask(__name__)
api = Api(app)


app.config['MONGODB_SETTINGS'] = {
    'db': 'User12',
    'host': 'localhost',
    'port': 27017
}
db = MongoEngine()
db.init_app(app)


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
			return ''
			# return Response(response=json.dumps({"message": ERROR_BAD_REQUEST, "status": 400}), status=400)

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
			return ''
			# return Response(response=json.dumps({"message": ERROR_BAD_REQUEST, "status": 400}), status=400)

from flask import Flask,request,make_response
import jwt
from flask import request
from datetime import datetime,timedelta
from flask_restful import Resource,Api
from .model import User,hash_password,check_password
import datetime
from flask_bcrypt import generate_password_hash,check_password_hash
from datetime import timedelta
from flask_jwt_extended import create_access_token,create_refresh_token

class Signup_Api(Resource):
	def post(self):
		try:
			body = request.get_json()
			user = User(**body)
			hash_password(user)
			user.save()
			id = user.id
			# return {'id': str(id)}, 200
			return jsonify({"result":"User Signup Successfully"})
		except Exception as error:
			logger.error("Error occurred => ", str(error))

class Login_Api(Resource):
	def post(self):
		try:
			body = request.get_json()
			user = User.objects.get(email=body.get('email'))
			authorized = check_password(body.get('password'))
			if not authorized:
				return {'error': 'Email or password invalid'}, 401
			expires = datetime.timedelta(days=7)
			access_token = create_access_token(identity=str(user.id), expires_delta=expires)
			return {'token': access_token}, 200
		except Exception as error:
			logger.error("Error occurred => ", str(error))


api.add_resource(Signup_Api,'/user_signup')
api.add_resource(Login_Api,'/user_Login')
api.add_resource(Market_Summary,'/market-data')

if __name__ == '__main__':
	app.run(debug=True)

