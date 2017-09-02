from flask import request, current_app, render_template
from . import routes

@routes.route('/model/<schema>')
def schema(schema):
    connstring = current_app.config["connstring"].to_dict()
    connstring.pop("password")
    curr = current_app.config["conn"].cursor()
    curr.execute("SELECT table_name FROM information_schema.tables WHERE table_schema LIKE '{}'".format(schema))
    rows = curr.fetchall()
    return render_template('schema.html', schema=schema, template=connstring, tables=rows)
