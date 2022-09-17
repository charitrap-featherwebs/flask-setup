from flask import Blueprint
from src.general.api import Homeview

general_url = Blueprint("general", __name__, url_prefix="")

general_url.add_url_rule(
            "/", 
            view_func=Homeview.as_view("homepage"), 
            methods=["GET", ]
        )
