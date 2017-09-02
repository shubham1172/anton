from flask import jsonify, request, current_app, abort, redirect
import psycopg2
from . import routes

@routes.route('/')
def index():
    if "conn" in current_app.config.keys():
        return redirect('/schemas')
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
    current_app.config["conn"] = conn
    current_app.config["connstring"] = request.form
    return redirect('/schemas')

@routes.route('/logout')
def logout():
    if "conn" in current_app.config.keys():
        current_app.config.pop("conn")
        current_app.config.pop("connstring")
        return jsonify(message="Logged out!")
    else:
        abort(403);
