from datetime import datetime
from datetime import timedelta
import jwt
from .config import SECRET_KEY


def generate_jwt_token(self):
    """
    Generates a JSON Web Token(JWT) for accessing the API.
    """
    dt = datetime.now() + timedelta(days=7)

    token = jwt.encode({
        'id': self.pk,
        'exp': dt
    }, SECRET_KEY, algorithm='HS256')

    return token