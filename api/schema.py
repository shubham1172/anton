# We are schema experts
from flask import current_app, request, session
from . import api
from . import sender
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
