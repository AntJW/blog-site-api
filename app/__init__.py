from flask import Flask
from flask_cors import CORS
from db import DBConnection
import configparser

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://anthonyjw.com"}})
config = configparser.ConfigParser()
config.read('config.ini')

conn = DBConnection()

from app.resources import posts, auth, contact, logger
