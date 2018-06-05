# Views blueprint init file
from flask import Blueprint, request, current_app, session

views = Blueprint('views', __name__, static_folder='static')
# Allowed URLs
allowed = ['views.index', 'views.login', 'views.logout']


# Conditional routing as per session
@views.before_request
def before_request():
    if request.endpoint not in allowed and "user-token" not in session:
        return redirect('/')


# Import errorhandler and routes
from .error_handler import *
from .auth import *
from .model import *
from .schema import *
from .table import *
