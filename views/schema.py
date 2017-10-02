from flask import render_template, abort, session
from . import views
from connections import getConnection

@views.route('/model/<schema>')
def schema(schema):
    conn, connstring = getConnection(session["user-token"])
    curr = conn.cursor()
    query = """SELECT table_name
                FROM information_schema.tables
                WHERE table_schema
                LIKE '{}'""".format(schema)
    try:
        curr.execute(query)
    except:
        abort(500)
    message = ""
    rows = curr.fetchall()
    if len(rows)==0:
        message = "No tables found. Schema name invalid/Schema is empty"
    return render_template('schema.html', message=message,
        schema=schema, template=connstring, tables=rows)

@views.route('/model/add-schema')
def add_schema():
    return render_template('schema_add.html', template=getConnection(session["user-token"])[1])

@views.route('/model/<schema>/rename')
def rename_schema(schema):
    return render_template('schema_rename.html', template=getConnection(session["user-token"])[1])
