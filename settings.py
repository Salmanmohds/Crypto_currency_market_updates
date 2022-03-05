from decouple import config

SECRET_KEY = config('SECRET_KEY', cast=str)
market_summary_url = config('market_summary_url', cast=str)
market_access_url = config('market_access_url', cast=str)

# market_summary_url='https://api.bittrex.com/api/v1.1/public/getmarketsummaries'
# market_access_url='https://api.bittrex.com/api/v1.1/public/getmarketsummary'
#
# SECRET_KEY='u4J9g1BJ0m2etnphSCqalw'