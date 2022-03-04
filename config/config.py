import datetime

market_summary_url="https://api.bittrex.com/api/v1.1/public/getmarketsummaries"
market_access_url="https://api.bittrex.com/api/v1.1/public/getmarketsummary"

SECRET_KEY="u4J9g1BJ0m2etnphSCqalw"

JWT_SECRET_KEY='t1NP63m4wnBg6nyHYKfmc2TpCOGI4nss'


JWT_AUTH = {
    'JWT_VERIFY': True,
    'JWT_VERIFY_EXPIRATION': True,
    'JWT_EXPIRATION_DELTA': datetime.timedelta(seconds=3000),
    'SIGNING_KEY': SECRET_KEY,
}

JWT_ALGORITHM = 'HS256'