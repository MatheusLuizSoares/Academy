from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = '123'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///academy.db"


db = SQLAlchemy(app)
migrate = Migrate(app ,db)

from app import routes







