from flask import Blueprint
from src.auth.api import LoginAPI, RegisterAPI

auth_url = Blueprint("auth", __name__, url_prefix="/api/v1")

auth_url.add_url_rule(
            "/login/", 
            view_func=LoginAPI.as_view("login"), 
            methods=["POST", ]
        )

auth_url.add_url_rule(
            "/register/", 
            view_func=RegisterAPI.as_view("register"), 
            methods=["POST", ]
        )
