from flask import request, session
from api import api, sender
from connections import getConnection

"""
Creates a schema
Requires:
Schema name -> schema
"""
@api.route('/create-schema', methods=["POST"])
def create_schema():
    name =  request.json['schema']
    if not name:
        return sender.BadRequest("missing field: schema")
    curr = getConnection(session["user-token"])[0].cursor()
    query = "CREATE SCHEMA \"{}\";".format(name)
    try:
        curr.execute(query)
        return sender.OK("Schema {} successfully created!".format(name))
    except Exception as e:
        return sender.Error(str(e))
