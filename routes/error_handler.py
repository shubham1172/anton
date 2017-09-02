from flask import jsonify, request
from . import routes

#Handle errors for Flask

@routes.errorhandler(403)
def forbidden(e):
    return jsonify(code = 403, message="forbidden")

@routes.errorhandler(405)
def not_allowed(e):
    return jsonify(code = 405, message="not allowed")
