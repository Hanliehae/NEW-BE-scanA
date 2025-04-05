from .auth_routes import auth_bp
from .admin_routes import admin_bp
from .user_routes import user_bp
from .scan_routes import scan_bp

def register_routes(app):
    app.register_blueprint(auth_bp, url_prefix='/auth')
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(user_bp, url_prefix='/user')
    app.register_blueprint(scan_bp, url_prefix='/scan')
