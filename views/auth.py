from flask import jsonify, request, abort, redirect, current_app, session, url_for, json
import requests
import psycopg2
from . import views
from connections import setConnection, getConnection, closeConnection

@views.route('/')
def index():
    #If logged in, redirect to model
    if "user-token" in session:
        return redirect('/model')
    return current_app.send_static_file('home.html')

@views.route('/login', methods=['POST'])
def login():
    #API URL
    url = request.url_root + url_for('api.login')[1:]
    try:
        data = json.loads(json.dumps(request.form))
        r = requests.post(url, json = data)
        res = r.json()
        if res["code"] == 200:
            #Set session for this blueprint
            session["user-token"] = res["args"]
            return redirect('/model')
        else:
            return redirect('/')
    except Exception as e:
        return str(e)

@views.route('/logout')
def logout():
    #API URL
    url = request.url_root + url_for('api.logout')[1:]
    try:
        r = requests.post(url)
        session.pop("user-token") #anyway have to remove it
        return redirect('/')
    except Exception as e:
        return str(e)
