from flask import Flask
from flask_sqlalchemy import SQLAlchemy 

#static files
App = Flask(__name__, static_url_path='/static')
App.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:r00t@localhost/complaints'
db = SQLAlchemy(App)

from app import routes
