#Main app file
from flask import Flask
from routes import *

app = Flask(__name__)
app.config.from_object('config') #load config
app.register_blueprint(routes, urlprefix='')

#Start app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
