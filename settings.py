from decouple import config

SECRET_KEY = config('SECRET_KEY', cast=str)

# Market-Api configuration
market_summary_url = config('market_summary_url', cast=str)
market_access_url = config('market_access_url', cast=str)

# Jwt_token

AUTH_TOKEN = config('AUTH_TOKEN', cast=str)