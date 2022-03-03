# from flask import Flask,request,make_response
# import jwt
# from flask import request
# from datetime import datetime,timedelta
# from flask_restful import Resource,Api
# from model import User
# app = Flask(__name__)
# api = Api(app)
# import datetime
# from datetime import timedelta
# from flask_jwt_extended import create_access_token,create_refresh_token
#
#
# class Signup_Api(Resource):
#     def post(self):
#         body = request.get_json()
#         user = User(**body)
#         user.hash_password()
#         user.save()
#         id = user.id
#         return {'id': str(id)}, 200
#
# class Login_Api(Resource):
#     def post(self):
#         body = request.get_json()
#         user = User.objects.get(email=body.get('email'))
#         authorized = user.check_password(body.get('password'))
#         if not authorized:
#             return {'error': 'Email or password invalid'}, 401
#         expires = datetime.timedelta(days=7)
#         access_token = create_access_token(identity=str(user.id), expires_delta=expires)
#         return {'token': access_token}, 200
#
#
# api.add_resource(Signup_Api,'/user_signup')
# api.add_resource(Login_Api,'/user_Login')
#
#
# if __name__ == '__main__':
#     app.run(debug=True)
#
#
