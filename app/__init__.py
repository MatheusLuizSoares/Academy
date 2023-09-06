from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt


app = Flask(__name__)

app.config['SECRET_KEY'] = '123'
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///academy.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
migrate = Migrate(app ,db)
bcrypt = Bcrypt(app)

from app import routes







