# We are schema experts
from flask import current_app, request, session
from . import api
from . import sender
from connections import getConnection

@api.route('/test')
def test():
    curr = getConnection(session["user-token"])[0].cursor()
    query = "SELECT * FROM public.test"
    try:
        curr.execute(query)
        return sender.OK(curr.fetchall())
    except Exception as e:
        return sender.Error(str(e))
"""
Creates a schema
Requires:
Schema name -> name
"""
@api.route('/create-schema', methods=['POST'])
def create_schema():
    name = request.form["name"]
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
@api.route('/drop-schema', methods=['POST'])
def drop_schema():
    name = request.form["name"]
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
