from flask import Blueprint, request, jsonify
from controllers.auth import *

auth = Blueprint("auth", __name__)

@auth.route("/register", methods=['POST'])
def register():
    data = request.get_json()
    return register_user(data.get("username"), data.get("password"))    

@auth.route("/login", methods=['POST'])
def login():
    data = request.get_json()
    return login_user(data.get("username"), data.get("password"))