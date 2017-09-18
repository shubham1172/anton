#Main app file
from flask import Flask
from views import *
from api import *

app = Flask(__name__)
app.config.from_object('config') #load config
app.register_blueprint(views, url_prefix='')
app.register_blueprint(api, url_prefix='/api')

#Start app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
