from flask import request, session
from api import api, sender
from connections import closeConnection

@api.route('/logout', methods=['POST'])
def logout():
    #Check if logged in
    if "user-token" in session:
        closeConnection(session["user-token"])
        session.pop("user-token")
        return sender.OK("Logged out!")
    else:
        return sender.OK("Login first!")