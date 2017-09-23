from flask import request, session, jsonify
from api import api, sender
from connections import getConnection

"""
Get schemas in database
"""
@api.route('/get-schemas')
def get_schemas():
    curr = getConnection(session["user-token"])[0].cursor()
    query = """SELECT schema_name FROM information_schema.schemata""";
    try:
        curr.execute(query)
        return sender.OK(curr.fetchall())
    except Exception as e:
        return sender.Error(str(e))
