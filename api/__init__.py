#API blueprint init file
from flask import Blueprint, current_app, session, request

api = Blueprint('api', __name__)
"""
This blueprint is the API for Anton
All the methods only support POSTed JSON
Don't forget to put
    'content-type as application/JSON in thy requests!'
"""

#Connection data
@api.before_request
def before_request():
    if "user-token" not in session:
        return sender.Forbidden("Login to use the API")
    if request.json is None:
        return sender.BadRequest("JSON expected")

#Import routes
from .sender import *
from .table_features import *
from .schema_features import *
