from flask import Blueprint
from src.general.api import Homeview

user_url = Blueprint("user", __name__, url_prefix="/api/v1/users")

user_url.add_url_rule(
            "/", 
            view_func=Homeview.as_view("user"), 
            methods=["GET", ]
        )
