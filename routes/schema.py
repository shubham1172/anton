from flask import jsonify, request, current_app, abort, render_template
import psycopg2
from . import routes

@routes.route('/schemas')
def schemas():
    connstring = current_app.config["connstring"]
    return render_template('schema.html', host=connstring["host"], port=connstring["port"])
