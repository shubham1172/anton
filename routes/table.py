from flask import request
from . import routes

@routes.route('/model/<schema>/<table>')
def table(schema,table):
    return "Table view"
