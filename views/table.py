from flask import request, render_template, abort, session
from . import views
from app import setConnection, getConnection, closeConnection

@views.route('/model/<schema>/<table>')
def table(schema,table):
    conn, connstring = getConnection(session["user-token"])
    curr = conn.cursor()
    query = """SELECT column_name, data_type
                FROM information_schema.columns
                WHERE table_name LIKE '{}'
                    AND table_schema LIKE '{}'""".format(table, schema)
    try:
        curr.execute(query)
    except:
        abort(500)
    message = ""
    rows = curr.fetchall()
    if len(rows)==0:
        message = "No columns found. Table name invalid/Table is empty"
    return render_template('table.html', message=message,
        schema=schema, table=table, template=connstring, columns=rows)
