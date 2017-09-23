from flask import request, session, jsonify
from api import api, sender
from connections import getConnection

"""
Get tables in a schema
Requires:
Schema name -> schema
"""
@api.route('/get-tables') #/get-tables?schema=schemaname
def get_tables():
    schema = request.args.get('schema')
    if not schema:
        return sender.BadRequest("Missing parameter: schema")
    curr = getConnection(session["user-token"])[0].cursor()
    query = """SELECT table_name FROM information_schema.tables
                WHERE table_schema = '{}'""".format(schema)
    try:
        curr.execute(query)
        rows = curr.fetchall()
        if len(rows) == 0:
            return sender.OK({"message": "Schema doesn't exists or is empty"})
        return sender.OK(rows)
    except Exception as e:
        return sender.Error(str(e))
