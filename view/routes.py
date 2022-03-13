from .market_api import Market_Summary,Home
from .auth import Signup_Api,Login_Api

def initialize_routes(api):
    api.add_resource(Signup_Api, '/user_signup')
    api.add_resource(Login_Api, '/user_Login')
    api.add_resource(Market_Summary, '/market-data')
    api.add_resource(Home, '/home')