from flask import Blueprint
from src.general.api import Homeview

general = Blueprint("general", __name__, url_prefix="/api/v1")

general.add_url_rule(
            "/", 
            view_func=Homeview.as_view("homepage"), 
            methods=["GET", ]
        )
