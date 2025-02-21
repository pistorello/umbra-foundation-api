# ROUTES

from flask import Blueprint, request, jsonify
from controllers.auth import *

auth = Blueprint("auth", __name__)

@auth.post("/register")
def register():
    data = request.get_json()
    return register_user(data.get("username"), data.get("password"))    

@auth.post("/login")
def login():
    data = request.get_json()
    return login_user(data.get("username"), data.get("password"))