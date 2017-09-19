from flask import jsonify, request, abort, redirect, current_app, session
import psycopg2
from . import views
from connections import setConnection, getConnection, closeConnection

@views.route('/')
def index():
    #If logged in, redirect to model
    if "user-token" in session:
        return redirect('/model')
    return current_app.send_static_file('index.html')

@views.route('/login', methods=['POST'])
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
        conn.set_session(autocommit=True)
    except:
        #Cannot connect
        abort(403);
    #Temporary dictionary to hold request info
    conndict = request.form.to_dict()
    conndict.pop("password")
    #Add object to session
    session["user-token"] = setConnection([conn, conndict])
    return redirect('/model')

@views.route('/logout')
def logout():
    #Check if logged in
    if "user-token" in session:
        closeConnection(session["user-token"])
        session.pop("user-token")
        return redirect('/')
    else:
        abort(405);
