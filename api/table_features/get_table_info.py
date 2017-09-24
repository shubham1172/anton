from flask import request, session, jsonify
from api import api
from api import sender
from connections import getConnection

"""
Get table info
Requires:
Table name -> table
Schema name -> schema (default is public)
Returns:
    {
        schema: schemaname,
        table: tablename,
        columns: [
            {
                name: columnNname,
                type: columnNtype,
                nullable: columnNnullable,
                default: columnNdefault
            }
        ]
    }
"""
@api.route('/get-table-info', methods=['POST'])
def get_table_info():
    tablename = request.json.get('table', None)
    schemaname = request.json.get('schema', None)
    if not tablename:
        return sender.BadRequest("missing field: table")
    if not schemaname:
        schemaname = "public"
    data = {}
    curr = getConnection(session["user-token"])[0].cursor()
    query = """SELECT
                table_schema,
                table_name,
                column_name,
                data_type,
                column_default,
                is_nullable
                    FROM information_schema.columns
                    WHERE table_name = '{}' AND table_schema = '{}';""".format(tablename, schemaname)
    try:
        curr.execute(query)
        rows = curr.fetchall()
        if len(rows) == 0:
            data["message"] = "Table doesn't exists or is empty"
        else:
            data["schema"] = rows[0][0]
            data["table"] = rows[0][1]
            data["columns"] = []
            for row in rows:
                data["columns"].append({
                    "name": row[2],
                    "type": row[3],
                    "default": row[4],
                    "nullable": row[5]
                })
        return sender.OK(data)
    except Exception as e:
        return sender.Error(str(e))
