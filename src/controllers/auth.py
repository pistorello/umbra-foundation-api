from flask import jsonify
from models.user import Users
from peewee import *
import bcrypt

def register_user(username, password):    
    if not username or not password:
        return jsonify({"message": "username e senha são obrigatórios."}), 400
    
    try:
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        Users.create(username=username, password=hashed_password)
        return jsonify({"message": "usuário registrado com sucesso."}), 201
    
    except IntegrityError:
        return jsonify({"message": "usuário já existe."}), 409
    
    except Exception as e:
        return jsonify({"message": "falha ao registrar usuário.", "error": str(e)}), 500
    
def login_user(username, password):
    if not username or not password:
        return jsonify({"message": "username e senha são obrigatórios."}), 400
    
    try:
        user = Users.get_or_none(Users.username == username)

        if user == None:
            return jsonify({"message": "usuário ou senha incorreto."}), 401

        if bcrypt.checkpw(password.encode('utf-8'), user.password):
            return jsonify({"message": "login realizado com sucesso."}), 200
        else:
            return jsonify({"message": "usuário ou senha incorreto."}), 401
        
    except DoesNotExist:
        return jsonify({"message": "usuário ou senha incorreto."}), 401
    
    except Exception as e:
        return jsonify({"message": "erro interno.", "erro": str(e)})