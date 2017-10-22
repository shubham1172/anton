from flask import request, session
from connections import getConnection
from api import api, sender

"""
Runs raw SQL
requires:
Raw query -> query
"""
@api.route('/raw-sql', methods=['POST'])
def raw_sql():
    query = request.json.get("query", None)
    if not query:
        return sender.BadRequest()
    curr = getConnection(session["user-token"])[0].cursor()
    try:
        curr.execute(query)
        return sender.OK(curr.fetchall())
    except Exception as e:
        return sender.Error(str(e))
