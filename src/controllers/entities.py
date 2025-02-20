from models.entity import Entities
from flask import jsonify
from peewee import *

def create(entity):
    if not entity.name:
        return jsonify({"message:": "nome é obrigatório."}), 400
    try:
        Entities.create(entity.name, entity.description, entity.image)
    except Exception as e:
        return jsonify({"message": "erro interno.", "error": str(e)})
    
def list(entities):
    pass

def update(entity):
    pass

def delete(entity):
    pass