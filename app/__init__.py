from flask import Flask
import sqlite3

app = Flask(__name__)

app.config['SECRET_KEY'] = '123'

from app import routes