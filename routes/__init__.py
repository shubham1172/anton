#Routes blueprint init file
from flask import Blueprint
routes = Blueprint('routes', __name__, static_folder='static')

from .auth import *
