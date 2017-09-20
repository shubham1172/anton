#API blueprint init file
from flask import Blueprint, current_app, session

api = Blueprint('api', __name__)

#Connection data
@api.before_request
def before_request():
    if "user-token" not in session:
        return sender.Forbidden("Login to use the API")

#Import routes
from .schema import *
from .sender import *
from .table import *
