# Main app file
from flask import Flask, render_template
from views import *
from api import *
import argparse

app = Flask(__name__)
app.config.from_object('config')    # load config
# Register blueprints
app.register_blueprint(views, url_prefix='')
app.register_blueprint(api, url_prefix='/api')


@app.before_first_request
def before_first_request():
    session.clear()


@app.route('/site-map')
def site_map():
    routes = []
    for rule in app.url_map.iter_rules():
        routes.append(rule)
    return render_template('sitemap.html', routes=routes)


# Start app
if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("-p", "--port", help="port number", nargs='?', const=80, type=int)
    args = parser.parse_args()
    app.run(host='0.0.0.0', port=args.port, threaded=True, debug=True)

# note: added threaded as true to support multiple requests in the debug server
# used while calling api functions from view requests
