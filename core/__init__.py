from flask import Flask
from src.general.routes import general

def create_app():
    application = Flask(
        __name__,
    )

    application.register_blueprint(general)

    return application
