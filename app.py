#Main app file
from flask import Flask, session
from views import *
from api import *

app = Flask(__name__)
app.config.from_object('config') #load config
### Register blueprints ###
app.register_blueprint(views, url_prefix='')
app.register_blueprint(api, url_prefix='/api')

@app.before_first_request
def before_first_request():
    session.clear()

#Start app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
