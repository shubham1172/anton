from flask import request, session
from api import api, sender
from connections import getConnection

"""
Creates a table
Requires:
{
    name: table_name,
    columns:[
        {
            name: col1,
            type: type1,
            length: len, //default none
            nullable: bool, //default true
            default: default_val, //default none
            unique: bool //default false
            primary_key: bool //default false
        },
        {
            ...
        }
    ]
}
"""
@api.route('/create-table', methods=['POST'])
def create_table():
    return "test"
