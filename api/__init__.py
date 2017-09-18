#API blueprint init file
from flask import Blueprint, current_app
from views import connection as routes_conn

api = Blueprint('api', __name__)

#Connection data
@api.before_request
def before_request():
    if routes_conn():
        current_app.config["conn"] = routes_conn()
    else:
        return sender.Forbidden("Login to use the API")

#Import routes
from .schema import *
from .sender import *
