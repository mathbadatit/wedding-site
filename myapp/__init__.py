import os
from flask import Flask, session, request, send_from_directory
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel
from flask_mail import Mail
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv

from .utils.error_handler_utils import register_error_handlers  # Gestore Errori

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
babel = Babel()
csrf = CSRFProtect()
login_manager = LoginManager()
jwt = JWTManager()

login_manager.login_view = 'admin.login'

load_dotenv()

def get_locale():
    lang = session.get('lang')
    if lang in ['it', 'en', 'ar']:
        return lang
    return request.accept_languages.best_match(['it', 'en', 'ar']) or 'it'

from myapp.models import (
    AdminUser,
    Service,
    GalleryImage,
    Collaborator
)

def create_app():
    app = Flask(__name__)

    # Config dinamica ambiente
    env = os.environ.get('FLASK_ENV', 'development')
    if env == 'production':
        from config import ProductionConfig
        app.config.from_object(ProductionConfig)
    else:
        from config import DevelopmentConfig
        app.config.from_object(DevelopmentConfig)

    os.makedirs(app.config.get('UPLOAD_FOLDER', 'uploads'), exist_ok=True)

    # Inizializzazione estensioni
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    babel.init_app(app, locale_selector=get_locale)
    csrf.init_app(app)
    login_manager.init_app(app)
    jwt.init_app(app)

 # ✅ Registrazione comandi CLI
    from .commands import register_commands
    register_commands(app)

    # Registrazione Blueprint
    from .main import bp as main_bp
    from .admin import bp as admin_bp
    from .booking import booking_bp
    from .contact import contact_bp
    from .api import api_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(booking_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(api_bp, url_prefix='/api')

    # User Loader
    from myapp.models.user import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @app.context_processor
    def inject_get_locale():
        return dict(get_locale=get_locale)

    @app.context_processor
    def inject_current_year():
        from datetime import datetime
        return {'current_year': datetime.now().year}

    @app.route('/uploads/<filename>')
    def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

    @app.route('/set_language/<lang_code>')
    def set_language(lang_code):
        if lang_code in ['it', 'en', 'ar']:
            session['lang'] = lang_code
        return request.referrer or '/'

    register_error_handlers(app)

    return app