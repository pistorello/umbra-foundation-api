from flask import Flask, jsonify, request
from models.user import Users
from controllers.auth import *
from routes import register
from peewee import *
import db_connection

app = Flask(__name__)
db_connection.startConnection()

register(app)

if __name__ == "__main__":
    app.run(debug=True)