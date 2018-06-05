from flask import session
from api import api, sender
from connections import getConnection


"""
Get schemas in database
"""
@api.route('/get-schemas', methods=['POST'])
def get_schemas():
    curr = getConnection(session["user-token"])[0].cursor()
    query = """SELECT schema_name FROM information_schema.schemata""";
    try:
        curr.execute(query)
        rows = [row[0] for row in curr.fetchall()]
        return sender.OK(rows)
    except Exception as e:
        return sender.Error(str(e))
