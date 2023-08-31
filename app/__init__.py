from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SECRET_KEY'] = '123'

from app import routes

db = SQLAlchemy(app)

app.config["SQLALCHEMY_DATABASE_URI"] = "SQLITE:///academy.db"
