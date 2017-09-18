#Views blueprint init file
from flask import Blueprint, request, current_app
views = Blueprint('views', __name__, static_folder='static')
#Allowed URLs
allowed = ['views.index', 'views.login', 'views.logout']

#Conditional routing as per session
@views.before_request
def before_request():
    if request.endpoint not in allowed and "conn" not in current_app.config.keys():
        return redirect('/')

#To be used in other blueprints
def connection():
    if "conn" in current_app.config:
        return current_app.config['conn']
    else:
        return None

#Import errorhandler and routes
from .error_handler import *
from .auth import *
from .model import *
from .schema import *
from .table import *
