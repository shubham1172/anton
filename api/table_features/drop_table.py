from flask import request, session
from api import api, sender
from connections import getConnection

"""
Drops a table
Requires:
Schema name -> schema
Table name -> table
"""
@api.route('/drop-table', methods=['POST'])
def drop_table():
    schema = request.json.get("schema", None)
    name = request.json.get("table", None)
    if not name:
        return sender.BadRequest()
    not_allowed = ["pg_toast", "pg_catalog","information_schema"]
    if not schema:
        schema = "public"
    if schema in not_allowed:
        return sender.Forbidden("Not allowed")
    curr = getConnection(session["user-token"])[0].cursor()
    query = "DROP TABLE \"{}\".\"{}\";".format(schema,name)
    try:
        curr.execute(query)
        return sender.OK("Table {} successfully dropped".format(name))
    except Exception as e:
        return sender.Error(str(e))
