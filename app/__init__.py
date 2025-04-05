from flask import Flask
from flask_migrate import Migrate
from app.config import Config
from .extensions import db
from app.models import *

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    # Register all blueprints using helper
    from app.routes import register_routes
    register_routes(app)

    return app
