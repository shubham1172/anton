from flask import jsonify, request
from . import views

#Handle errors for Flask

@views.errorhandler(403)
def forbidden(e):
    return jsonify(code = 403, message="forbidden")

@views.errorhandler(405)
def not_allowed(e):
    return jsonify(code = 405, message="not allowed")

@views.errorhandler(500)
def server_error(e):
    return jsonify(code = 500, message="server error")
