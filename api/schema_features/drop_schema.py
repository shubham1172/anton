from flask import request, session
from api import api, sender
from connections import getConnection


"""
Drops a schema
Requires:
Schema name -> schema
"""
@api.route('/drop-schema', methods=['POST'])
def drop_schema():
    name = request.json.get('schema', None)
    if not name:
        return sender.BadRequest("missing field: schema")
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
