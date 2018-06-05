from flask import request, session
from api import api, sender
from connections import getConnection


"""
Renames a schema
Requires:
Table name -> schema
New name -> new_name
"""
@api.route('/rename-schema', methods=['POST'])
def rename_schema():
    name = request.json.get('schema', None)
    new_name = request.json.get('new_name', None)
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
