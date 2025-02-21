# ROUTES

from flask import Blueprint, request, jsonify
from models.entity import Entities
import controllers.entities as entities_controller

entities = Blueprint("entities", __name__)

@entities.post("/")
def create():
    data = request.get_json()
    return entities_controller.create(data)

@entities.get("/")
def list():
    data = request.get_json()
    return entities_controller.list(data)

@entities.put("/<int:id>")
def update(id):
    data = request.get_json()
    return entities_controller.update(id, data)

@entities.delete("/<int:id>")
def delete(id):
    return entities_controller.delete(id)