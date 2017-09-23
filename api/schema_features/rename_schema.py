from flask import request, session, jsonify
from api import api, sender
from connections import getConnection

"""
Renames a schema
Requires:
Old name -> name
New name -> new_name
"""
@api.route('/rename-schema') #/rename-schema?name=schemaname&new_name=newschema
def rename_schema():
    name = request.args.get('name')
    new_name = request.args.get('new_name')
    if not name or not new_name:
        return sender.BadRequest()
    not_allowed = ["pg_toast", "pg_catalog","public","information_schema"]
    if name in not_allowed:
        return sender.Forbidden("Not allowed")
    curr = getConnection(session["user-token"])[0].cursor()
    query = "ALTER SCHEMA \"{}\" RENAME TO \"{}\";".format(name, new_name)
    try:
        curr.execute(query)
        return sender.OK("Schema {} successfully renamed to {}!".format(name, new_name))
    except Exception as e:
        return sender.Error(str(e))
