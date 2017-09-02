from flask import jsonify, request, current_app, abort, render_template
import psycopg2
from . import routes

@routes.route('/schemas')
def schemas():
    connstring = current_app.config["connstring"].to_dict()
    #Create a template dict
    connstring.pop("password")
    curr = current_app.config["conn"].cursor()
    curr.execute('SELECT schema_name FROM information_schema.schemata')
    rows = curr.fetchall()
    return render_template('schema.html', template=connstring, schemas=rows)
