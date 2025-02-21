from .auth import auth
from .entities import entities

def register(app):
    app.register_blueprint(auth, url_prefix="/auth")
    app.register_blueprint(entities, url_prefix="/entities")
