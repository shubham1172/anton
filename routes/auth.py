from flask import jsonify, request, current_app, g
import psycopg2
from . import routes

@routes.route('/')
def index():
    return current_app.send_static_file('index.html')

@routes.route('/login', methods=['POST'])
def login():
    username = request.form["username"]
    password = request.form["password"]
    host = request.form["host"]
    port = request.form["port"]
    connstring = "dbname='postgres' user='{}' host='{}' password='{}' port={}".format(username, host, password, port)
    try:
        conn = psycopg2.connect(connstring)
    except Exception as e:
        return jsonify(error = str(e), message = 'Cannot connect for {}'.format(connstring))
    g.conn = conn
    return jsonify(message='Connected!')
