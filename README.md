# Crypto_currency_market_updates

This repository will keep the latest update of all the markets. It will refer to the data made available by bitrix.

Signup Api:- User need to be signup first with the following details {email, password, mobile_number}. It will store in the MongoDB.

Login api- Will generate JWT token using the username(username should be email) and password  entered by the user.

Market_summary:- This api will return all the market details via a GET request. But user will need to be authenticated via JWT token passed in the authorization request(Bearer Token)

Get_Particular_Market_Updates:- This api will return details of a specific market passed in the request param. Here user need to be pass starting with 3 letter - and ending with 3 letter(ex:- btc-itc). Implemented validation in Swagger file.

Run pip install -r requirements.txt to install dependencies to your local repository

#To run via docker ### Install docker and docker-compose on your machine and then RUN docker-compose up

# For test cases I referred Official documentation below:->
   # https://flask.palletsprojects.com/en/2.0.x/testing/