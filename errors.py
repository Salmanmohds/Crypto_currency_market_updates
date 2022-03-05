# # Custom exception handling
#
# class InternalServerError(Exception):
#     pass
#
# class SchemaValidationError(Exception):
#     pass
#
# class EmailAlreadyExistsError(Exception):
#     pass
#
# class UnauthorizedError(Exception):
#     pass
#
# class UnauthorizedTokenError(Exception):
#     pass
#
# errors = {
#     "InternalServerError": {
#         "message": "Something went wrong",
#         "status": 500
#     },
#     "SchemaValidationError": {
#          "message": "Request is provide required fields",
#          "status": 400
#      },
#     "EmailAlreadyExistsError": {
#          "message": "User with given email address already exists",
#          "status": 400
#      },
#     "UnauthorizedTokenError": {
#          "message": "Please provide valid token",
#          "status": 401
#      },
#     "UnauthorizedError": {
#          "message": "Invalid username or password",
#          "status": 401
#      }
# }