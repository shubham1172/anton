from flask import request, current_app, render_template
from . import routes

#Get all schemas in the database
@routes.route('/model')
def model():
    connstring = current_app.config["connstring"]
    curr = current_app.config["conn"].cursor()
    query = """SELECT schema_name
                FROM information_schema.schemata"""
    try:
        curr.execute(query)
    except:
        abort(500)
    rows = curr.fetchall()
    return render_template('model.html', template=connstring, schemas=rows)
