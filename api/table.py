# We do things under the table
from flask import request, session, jsonify
from . import api
from . import sender
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
@api.route('/get-table-info') #/get-table-info?table=tablename&schema=schemaname
def get_table_info():
    tablename = request.args.get('table')
    schemaname = request.args.get('schema')
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

"""
Get table data
Requires:
Table name -> table
Schema name -> schema (default is public)
Returns:

"""
@api.route('/get-table-data') #/get-table-data?table=tablename&schema=schemaname
def get_table_data():
    tablename = request.args.get("table")
    schemaname = request.args.get("schema")
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
            data["values"] = rows
        return sender.OK(data)
    except Exception as e:
        return sender.Error(str(e))
