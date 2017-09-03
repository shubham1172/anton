#Routes blueprint init file
from flask import Blueprint, request, current_app
routes = Blueprint('routes', __name__, static_folder='static')
#Allowed URLs
allowed = ['routes.index', 'routes.login', 'routes.logout']

#Set first to False
@routes.before_app_first_request
def before_app_first_request():
    current_app.config["first"] = False

#Conditional routing as per session
@routes.before_request
def before_request():
    if request.endpoint not in allowed and "conn" not in current_app.config.keys():
        return redirect('/')

#Import errorhandler and routes
from .error_handler import *
from .auth import *
from .model import *
from .schema import *
from .table import *
