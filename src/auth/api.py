from flask import request
from flask.views import MethodView

from src.auth.services import login, register


class LoginAPI(MethodView):
    def post(self):
        data = {
            'email': request.form.get('email', None),
            'password': request.form.get('password', None)
        }
        try:
            res = login(data)
            return res
        except Exception as e:
            print(e, " LoginAPI view error")
            return {"error": "Login failed"}, 500


class RegisterAPI(MethodView):
    def post(self):
        req_data = request.get_json()
        try:
            res = register(req_data)
            return res
        except Exception as e:
            print(e, " RegisterAPI view error")
            return {"error": "Register failed"}, 500