from flask import jsonify, request
from . import routes

@routes.errorhandler(403)
def forbidden(e):
    return jsonify(code = 403, message="not allowed")
