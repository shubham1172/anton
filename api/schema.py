# We are schema experts
from flask import current_app, request
from . import api
from . import sender

@api.route('/test')
def test():
    curr = current_app.config["conn"].cursor()
    query = """SELECT * FROM public.test"""
    try:
        curr.execute(query)
        rows = curr.fetchall()
        return sender.OK(rows)
    except Exception as e:
        return sender.Error(e)

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
    curr = current_app.config["conn"].cursor()
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
    curr = current_app.config["conn"].cursor()
    query = "DROP SCHEMA \"{}\";".format(name)
    try:
        curr.execute(query)
        return sender.OK("Schema {} successfully dropped!".format(name))
    except Exception as e:
        return sender.Error(str(e))
