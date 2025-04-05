from flask import Flask
from flask_migrate import Migrate
from app.config import Config
from app.extensions import db
from app.models import *  # pastikan model kehadiran, jadwal, dll. sudah di-import
from dotenv import load_dotenv
import os

migrate = Migrate()

def create_app(config_class=Config):
    load_dotenv()  # Load .env saat app dibuat

    app = Flask(__name__)
    app.config.from_object(config_class)

    # Init extensions
    db.init_app(app)
    migrate.init_app(app, db)

    # Register all blueprints
    from app.routes.auth_routes import auth_bp
    from app.routes.admin_routes import admin_bp
    from app.routes.user_routes import user_bp
    from app.routes.scan_routes import scan_bp

    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(scan_bp, url_prefix='/scan')

    return app
