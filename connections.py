from random import choice
from string import ascii_letters

#Dictionary maintaining record
logged_in = {}

"""
Sets connection for a user
Adds connection obj[conn, connstring] to config
Returns userToken that will be added to session
"""
def setConnection(connection):
    userToken = getRandomToken()
    logged_in[userToken] = connection
    return userToken

"""
Get connection obj for current user
"""
def getConnection(userToken):
    return logged_in[userToken]

"""
Close current connection obj
"""
def closeConnection(userToken):
    logged_in[userToken][0].close()
    logged_in.pop(userToken)

"""
Create a random token
"""
def getRandomToken():
    return ''.join(choice(ascii_letters) for i in range(10))
