from flask import request, session
from api import api, sender
from connections import getConnection

"""
Renames a table
Requires:
Schema name -> schema
Table name -> table
New name -> new_name
"""
@api.route('/rename-table', methods=['POST'])
def rename_table():
    schema = request.json.get("schema", None)
    name = request.json.get("table", None)
    new_name = request.json.get("new_name", None)
    if not name or not new_name:
        return sender.BadRequest()
    not_allowed = ["pg_toast", "pg_catalog","information_schema"]
    if schema in not_allowed:
        return sender.Forbidden("Not allowed")
    if not schema:
        schema = "public"
    curr = getConnection(session["user-token"])[0].cursor()
    query = """ALTER TABLE {}.{}
                RENAME TO \"{}\"""".format(schema,name,new_name)
    try:
        curr.execute(query)
        return sender.OK("Table {} successfully renamed to {}".format(name, new_name))
    except Exception as e:
        return sender.Error(str(e))
