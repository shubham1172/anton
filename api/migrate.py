from flask import request, session, send_from_directory, jsonify
from connections import getConnection, getRandomToken
from api import api, sender
import json

"""
EXPORT data
Returns json data
requires:
table: table_name
schema: schema_name
"""
@api.route('/export-table', methods=['POST'])
def export_table():
    table_name = request.json.get('table', None)
    schema_name = request.json.get('schema', None)
    if not table_name:
        return sender.BadRequest("missing field: table")
    if not schema_name:
        schema_name = "public"
    curr = getConnection(session["user-token"])[0].cursor()
    #get columns info
    col_query = """SELECT *
                FROM information_schema.columns
                WHERE table_name = '{}'
                AND table_schema = '{}';""".format(table_name, schema_name)
    #get columns data
    data_query = """SELECT *
                FROM {}.\"{}\"""".format(schema_name, table_name)
    try:
        curr.execute(col_query)
        col_rows = curr.fetchall()
        data = {}
        if len(col_rows)==0:
            data["message"]="Table does not exists"
        else:
            data["columns"]= [rows[3:] for rows in col_rows]
        curr.execute(data_query)
        val_rows = curr.fetchall()
        data["values"] = val_rows
        return jsonify(data)
    except Exception as e:
        return sender.Error(str(e))

"""
IMPORT data
requires:
table: new table_name //should not exist
schema: schema_name
data: json data which was exported
"""
@api.route('/import-table', methods=['POST'])
def import_table():
    table_name = request.json.get('table', None)
    schema_name = request.json.get('schema', None)
    data = request.json.get('data', None)
    if not table_name or not data:
        return sender.BadRequest()
    if not schema_name:
        schema_name = "public"
    try:
        conn, connstring = getConnection(session["user-token"])
        username = connstring["username"]
        curr = conn.cursor()
        check_query = """SELECT * FROM information_schema.tables WHERE
                    table_name='{}'
                    AND table_schema='{}'""".format(table_name, schema_name)
        curr.execute(check_query)
        if(len(curr.fetchall())!=0):
            return sender.Error("Table already exists. Remove it to import")
        #create table
        create_query = """CREATE TABLE {}.\"{}\"(""".format(schema_name, table_name)
        for items in data["columns"]:
            create_query=create_query+items[0]+" "+items[4]
            if items[3]=="NO":
                create_query=create_query+" NOT NULL"
            if items[2]:
                create_query=create_query+" DEFAULT "+items[2]
            create_query=create_query+","
        create_query=create_query[:-1]+");"
        curr.execute(create_query)
        #insert data
        insert_query = """INSERT INTO {}.\"{}\" VALUES""".format(schema_name, table_name)
        insert_query = insert_query + "(%s"+", %s"*(len(data["values"][0])-1)+")"
        curr.executemany(insert_query, data["values"])
        return sender.OK("Data imported successfully!")
    except Exception as e:
        return sender.Error(str(e))
