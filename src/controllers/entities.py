# CONTROLLER

from models.entity import Entities
from flask import jsonify
from peewee import *

def create(entity):
    if not entity.get("name"):
        return jsonify({"message": "nome é obrigatório."}), 400
    
    try:
        Entities.create(name=entity.get("name"), description=entity.get("description"), image=entity.get("image"))
        return jsonify({"message": "entidade criada com sucesso."}), 201
    
    except Exception as e:
        return jsonify({"message": "erro interno.", "error": str(e)}), 500
    
def list(entities):
    entities_ids = entities.get("ids") if entities else None
    
    if not entities_ids:
        entities_list = Entities.select()
    else:
        entities_list = Entities.select().where(Entities.id.in_(entities_ids))

    entities_json = [
        {"id": entity.id, "name": entity.name, "description": entity.description, "image": entity.image} 
        for entity in entities_list     
    ]

    if len(entities_list) == 0:
        return jsonify({"message": "nenhuma entidade encontrada."}), 404
        
    return jsonify({"result": entities_json}), 200

def update(id, entity):
    if id <= 0:
        return jsonify({"message": "id é obrigatório."}), 400
    
    try:
        entity_model = Entities.get_or_none(Entities.id == id)
        if not entity_model:
            return jsonify({"message": "entidade não encontrada."}), 404
        
        Entities.update(
            name=entity.get("name"), 
            description=entity.get("description"), 
            image=entity.get("image")
        ).where(Entities.id == id).execute()
        
        return jsonify({"message": "entidade atualizada com sucesso."}), 200
    except Exception as e:
        return jsonify({"message": "erro interno.", "error": str(e)}), 500


def delete(id):
    if id <= 0:
        return jsonify({"message": "id é obrigatório."}), 400
    
    try:
        entity_model = Entities.get_or_none(Entities.id == id)
        if not entity_model:
            return jsonify({"message": "entidade não encontrada."}), 404
        
        entity_model.delete_instance()
        return jsonify({"message": "entidade excluída com sucesso."}), 200

    except Exception as e:
        return jsonify({"message": "erro interno", "error": str(e)}), 500