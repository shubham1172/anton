#API blueprint init file
from flask import Blueprint, current_app, request, json, session

api = Blueprint('api', __name__)
"""
This blueprint is the API for Anton
All the methods only support POSTed JSON
Don't forget to put
    'content-type as application/JSON in thy requests!'
"""
#These endpoints donot require auth
allowed = ['api.login', 'api.logout']
#These endpoints donot require json
no_json = ['api.logout', 'api.get_schemas']

#Connection data
@api.before_request
def before_request():
    if request.endpoint not in allowed and "user-token" not in session:
        return sender.Forbidden("Login to use the API")
    if request.endpoint not in no_json and request.json is None:
        return sender.BadRequest("JSON expected")

#Import routes
from .sender import *
from .table_features import *
from .schema_features import *
from .authorization import *
