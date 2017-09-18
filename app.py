#Main app file
from flask import Flask, session
from views import *
from api import *
from random import choice
from string import ascii_letters

app = Flask(__name__)
app.config.from_object('config') #load config
app.register_blueprint(views, url_prefix='')
app.register_blueprint(api, url_prefix='/api')
app.config["logged_in"] = {} #logged in dictionary

@app.before_first_request
def before_first_request():
    session.clear()

"""
Sets connection for a user
Adds connection obj[conn, connstring] to config
Returns userToken that will be added to session
"""
def setConnection(connection):
    userToken = ''.join(choice(ascii_letters) for i in range(10))
    app.config["logged_in"][userToken] = connection
    return userToken

"""
Get connection obj for current user
"""
def getConnection(userToken):
    return app.config["logged_in"][userToken]

"""
Close current connection obj
"""
def closeConnection(userToken):
    app.config["logged_in"][userToken][0].close()
    app.config["logged_in"].pop(userToken)

#Start app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
