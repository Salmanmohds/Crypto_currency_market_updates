from app import app
from database.model import User
from unittest.mock import patch,Mock
from view.auth import Signup_Api,Login_Api

# class SignupTest(BaseCase):
# @patch('flask.request')

@patch('view.auth.request.get_json')
def test_successful_signup(get_json_mock):
    # payload = {
    #     "email": "roman13@gmail.com",
    #     "password": "roman13",
    #     "mobile_number": "5141325250"
    # }
    with app.test_client() as c:
        data = c.post('view/auth', json={
            'email': 'roman1354@gmail.com', 'password': 'roman1378',
            "mobile_number":"9857424184"
        })

        get_json_mock.return_value = {
            'email': 'roman1354@gmail.com', 'password': 'roman1378',
            "mobile_number":"9857424184"
        }
        json_data = data.get_json()
        signup_inst = Signup_Api()
        user_mock = User(**json_data)
        user_mock.hash_password = Mock(return_value=True)
        user_mock.save = Mock(return_value=True)
        # response = signup_inst.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)
        # request = Mock()
        # request_mock.get_json.return_value = payload
        response = signup_inst.post()
        assert response == {"result":"User Signup Successfully"}
        # self.assertEqual(200, response.status_code)


# @patch('flask.request.get_json')
# def test_successful_login(get_json_mock):
#     with app.test_client() as c:
#         data = c.post('/api/auth', json={
#             'email': 'roman13@gmail.com', 'password': 'roman1378',
#         })
#         get_json_mock.return_value = {
#             'email': 'roman1354@gmail.com', 'password': 'roman1378',
#             "mobile_number": "9857424184"
#         }
#         json_data = data.get_json()
#         login_inst = Login_Api()
#         user_mock = User(json_data)
#         user_mock.check_password = Mock(return_value=True)
#         response = login_inst.post()
        # response = self.app.post('/api/auth/signup', headers={"Content-Type": "application/json"}, data=payload)
        # response = self.app.post('/api/auth/login', headers={"Content-Type": "application/json"}, data=payload)
        # self.assertEqual(str, type(response.json['token']))
        # self.assertEqual(200, response.status_code)


