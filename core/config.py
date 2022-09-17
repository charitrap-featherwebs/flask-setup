import os
from datetime import timedelta

from dotenv import load_dotenv
load_dotenv()

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URI']
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "flask-secret-key"
JWT_SECRET_KEY = "jwt-secret-key"
JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
