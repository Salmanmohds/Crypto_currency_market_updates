from flask import Flask
from flask_jwt_extended import JWTManager
from Crypto_currency_market_updates.database.db import initialize_db
from flask_restful import Api
from Crypto_currency_market_updates.view.errors import errors
from flask_swagger_ui import get_swaggerui_blueprint
from Crypto_currency_market_updates.view.market_api import market_apis as market_data_blueprint
from Crypto_currency_market_updates.view.auth import auth_apis as auth_blueprint

def create_app():
    app = Flask(__name__)
    api = Api(app, errors=errors)

    jwt = JWTManager(app)

    # Swagger configuration
    SWAGGER_URL = '/api/swagger'
    API_URL = '/static/swagger.json'
    SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
        SWAGGER_URL,
        API_URL,
        config={
                'app_name': "Flask-REST-API"
            }
        )
    app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
    app.register_blueprint(market_data_blueprint, url_prefix='/api')
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    # MongoDB configuration

    # This configuration need to be use when we are running our application through Docker-compose
    app.config['MONGODB_SETTINGS'] = {
        'host': 'mongodb://mongo_db:27017/User12'
    }

    # This configuration need to be use when we are running our application locally.
    app.config['MONGODB_SETTINGS'] = {
        'host': 'mongodb://localhost/User12'
        }

    # JWT configuration
    app.config["JWT_SECRET_KEY"] = "super-secret"

    initialize_db(app)
    return app