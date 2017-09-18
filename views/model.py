from flask import request, current_app, render_template, abort
from . import views

#Get all schemas in the database
@views.route('/model')
def model():
    connstring = current_app.config["connstring"]
    curr = current_app.config["conn"].cursor()
    query = """SELECT schema_name
                FROM information_schema.schemata"""
    try:
        curr.execute(query)
    except Exception as e:
        print(e)
        abort(500)
    rows = curr.fetchall()
    return render_template('model.html', template=connstring, schemas=rows)
