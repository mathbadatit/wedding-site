import os
import logging
import traceback
from flask import Flask, session, request, redirect, url_for, send_from_directory, render_template
from myapp.extensions import db, migrate, mail, babel, csrf, login_manager, jwt
from myapp.auth.routes import bp as auth_bp
from myapp.utils.template_helpers import login_url
from flask import Blueprint, render_template
from myapp.models import Service

services_bp = Blueprint('services', __name__, url_prefix='/services')

@services_bp.route('/')
def list():
    services = Service.query.all()
    categories = sorted(set([s.category for s in services if s.category]))
    return render_template('services.html', services=services, categories=categories)

@services_bp.route('/modal/<int:service_id>')
def modal(service_id):
    service = Service.query.get_or_404(service_id)
    return render_template('partials/service_modal.html', service=service)


basedir = os.path.abspath(os.path.dirname(__file__))

def get_locale():
    lang = session.get('lang')
    if lang in ['it', 'en', 'ar']:
        return lang
    return request.accept_languages.best_match(['it', 'en', 'ar']) or 'it'

def create_app():
    app = Flask(__name__)

    env = os.environ.get('FLASK_ENV', 'development')
    if env == 'production':
        from config import ProductionConfig
        app.config.from_object(ProductionConfig)
    else:
        from config import DevelopmentConfig
        app.config.from_object(DevelopmentConfig)

    # Cartella upload
    app.config['UPLOAD_FOLDER'] = os.path.join(basedir, 'static', 'uploads')
    os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

    # Inizializza estensioni
    db.init_app(app)
    migrate.init_app(app, db)
    mail.init_app(app)
    babel.init_app(app, locale_selector=get_locale)
    csrf.init_app(app)
    login_manager.init_app(app)
    jwt.init_app(app)

    # Blueprint
    from myapp.main import bp as main_bp
    from myapp.admin import bp as admin_bp
    from myapp.booking import booking_bp
    from myapp.contact import contact_bp
    from myapp.api import api_bp

    app.register_blueprint(main_bp)
    app.register_blueprint(admin_bp, url_prefix='/admin')
    app.register_blueprint(booking_bp)
    app.register_blueprint(contact_bp)
    app.register_blueprint(api_bp, url_prefix='/api')
    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(services_bp)
    
    # User loader per login_manager
    from myapp.models.user import User
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id)) if user_id else None


    # Context processors
    @app.context_processor
    def inject_get_locale():
        return dict(get_locale=get_locale)

    @app.context_processor
    def inject_current_year():
        from datetime import datetime
        return {'current_year': datetime.now().year}
    
    @app.context_processor
    def inject_template_helpers():
       return dict(login_url=login_url)


    # Route per upload statico (immagini)
    @app.route('/uploads/<filename>')
    def uploaded_file(filename):
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

    # Route cambio lingua
    @app.route('/set_language/<lang_code>')
    def set_language(lang_code):
        if lang_code in ['it', 'en', 'ar']:
            session['lang'] = lang_code
        return redirect(request.referrer or url_for('main.home'))

    # Gestione errore 500
    @app.errorhandler(500)
    def internal_error(error):
        logging.error(f"Errore 500: {error}")
        traceback.print_exc()
        return render_template('500.html'), 500

    # Error handlers personalizzati
    from myapp.utils.error_handler_utils import register_error_handlers
    register_error_handlers(app)

    return app
