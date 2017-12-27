from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.secret_key = 'x'

db = SQLAlchemy(app)

#import routes
from app import flask_quickstart
##other imports

