from flask import request
from flask.views import MethodView

class Homeview(MethodView):

    def get(self):
        return "Hello world !!!"
