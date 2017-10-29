from flask import request, session, jsonify
from api import api
from api import sender
from connections import getConnection

"""
Get table data
Requires:
Table name -> table
Schema name -> schema (default is public)
Returns:

"""
@api.route('/get-table-data', methods=['POST'])
def get_table_data():
    tablename = request.json.get('table', None)
    schemaname = request.json.get('schema', None)
    if not tablename:
        return sender.BadRequest("missing field: table")
    if not schemaname:
        schemaname = "public"
    curr = getConnection(session["user-token"])[0].cursor()
    query = """SELECT *
                FROM {}.{}
                LIMIT 20""".format(schemaname,tablename)
    try:
        curr.execute(query)
        rows = curr.fetchall()
        data = {}
        if len(rows) == 0:
            data["message"] = "Table doesn't exists or is empty"
        else:
            data["headers"] = [desc[0] for desc in curr.description]
            dataQuery = """SELECT data_type FROM
                information_schema.columns WHERE
                table_name = '{}' AND table_schema = '{}';""".format(tablename,schemaname);
            curr.execute(dataQuery);
            data["types"] = [type[0] for type in curr.fetchall()]
            data["values"] = rows
        return sender.OK(data)
    except Exception as e:
        return sender.Error(str(e))
