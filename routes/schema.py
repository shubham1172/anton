from flask import request, current_app, render_template, abort
from . import routes

@routes.route('/model/<schema>')
def schema(schema):
    connstring = current_app.config["connstring"]
    curr = current_app.config["conn"].cursor()
    try:
        curr.execute("SELECT table_name FROM information_schema.tables WHERE table_schema LIKE '{}'".format(schema))
    except:
        abort(500)
    message = ""
    rows = curr.fetchall()
    if len(rows)==0:
        message = "No tables found. Schema name invalid/Schema is empty"
    return render_template('schema.html', message=message, schema=schema, template=connstring, tables=rows)
