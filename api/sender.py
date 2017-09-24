# Handles returning of data in a standard format
from flask import jsonify

def OK(data, args = None):
    if args:
        return jsonify(code=200, data=data, args=args)
    return jsonify(code=200, data=data)

def BadRequest(message="incorrect parameters"):
    return jsonify(code=400, message=message)

def Forbidden(message):
    return jsonify(code=403, message=message)

def Error(message):
    return jsonify(code=500, message=message)
