from flask import request, session, jsonify
from api import api, sender
from connections import getConnection

"""
Creates a schema
Requires:
Schema name -> name
"""
@api.route('/create-schema') #/create-schema?name=schemaname
def create_schema():
    name =  request.args.get('name')
    if not name:
        return sender.BadRequest("missing field: name")
    curr = getConnection(session["user-token"])[0].cursor()
    query = "CREATE SCHEMA \"{}\";".format(name)
    try:
        curr.execute(query)
        return sender.OK("Schema {} successfully created!".format(name))
    except Exception as e:
        return sender.Error(str(e))
