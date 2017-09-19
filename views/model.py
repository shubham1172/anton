from flask import request, render_template, abort, session
from connections import getConnection
from . import views

#Get all schemas in the database
@views.route('/model')
def model():
    conn, connstring = getConnection(session["user-token"])
    curr = conn.cursor()
    query = """SELECT schema_name
                FROM information_schema.schemata"""
    try:
        curr.execute(query)
    except Exception as e:
        print(e)
        abort(500)
    rows = curr.fetchall()
    return render_template('model.html', template=connstring, schemas=rows)
