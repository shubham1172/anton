#Routes blueprint init file
from flask import Blueprint, request
routes = Blueprint('routes', __name__, static_folder='static')
allowed = ['routes.index', 'routes.login', 'routes.logout']

@routes.before_request
def before_request():
    if request.endpoint not in allowed and "conn" not in current_app.config.keys():
        return redirect('/')

from .auth import *
from .schema import *
from .error_handler import *
