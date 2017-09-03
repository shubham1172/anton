from flask import jsonify, request, current_app, abort, redirect
import psycopg2
from . import routes

@routes.route('/')
def index():
    #If logged in, redirect to schemas
    if "conn" in current_app.config.keys():
        return redirect('/model')
    return current_app.send_static_file('index.html')

@routes.route('/login', methods=['POST'])
def login():
    #Collect form data
    username = request.form["username"]
    password = request.form["password"]
    host = request.form["host"]
    port = request.form["port"]
    #Create a connstring
    connstring = "dbname='postgres' user='{}' host='{}' password='{}' port={}".format(username, host, password, port)
    try:
        #Try to connect
        conn = psycopg2.connect(connstring)
    except:
        #Cannot connect
        abort(403);
    #Add objects to config file to be used later
    current_app.config["conn"] = conn
    #Temporary dictionary to hold request info
    conndict = request.form.to_dict()
    conndict.pop("password")
    current_app.config["connstring"] = conndict
    return redirect('/model')

@routes.route('/logout')
def logout():
    #Check if logged in
    if "conn" in current_app.config.keys():
        current_app.config.pop("conn")
        current_app.config.pop("connstring")
        return jsonify(message="Logged out!")
    else:
        abort(405);
