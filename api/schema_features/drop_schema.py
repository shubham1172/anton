from flask import request, session, jsonify
from api import api, sender
from connections import getConnection

"""
Drops a schema
Requires:
Schema name -> name
"""
@api.route('/drop-schema') #/drop-schema?name=schemaname
def drop_schema():
    name = request.args.get('name')
    if not name:
        return sender.BadRequest("missing field: name")
    not_allowed = ["pg_toast", "pg_catalog","public","information_schema"]
    if name in not_allowed:
        return sender.Forbidden("Not allowed")
    curr = getConnection(session["user-token"])[0].cursor()
    query = "DROP SCHEMA \"{}\";".format(name)
    try:
        curr.execute(query)
        return sender.OK("Schema {} successfully dropped!".format(name))
    except Exception as e:
        return sender.Error(str(e))
