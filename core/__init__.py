from flask import Flask

from dotenv import load_dotenv
load_dotenv()

from src.general.routes import general_url
from src.users.routes import user_url
from src.auth.routes import auth_url
from core.db import db


def create_app():
    application = Flask(
        __name__,
    )
    application.config.from_pyfile('config.py')
    db.init_app(application)

    application.register_blueprint(general_url)
    application.register_blueprint(user_url)
    application.register_blueprint(auth_url)

    return application
