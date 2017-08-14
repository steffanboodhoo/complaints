from flask import Flask

#static files
App = Flask(__name__, static_url_path='/static')

from app import routes
