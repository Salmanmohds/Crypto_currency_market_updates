from decouple import config

SECRET_KEY = config('SECRET_KEY', cast=str)
market_summary_url = config('market_summary_url', cast=str)
market_access_url = config('market_access_url', cast=str)