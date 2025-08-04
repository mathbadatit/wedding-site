from flask import Blueprint, request, session

bp = Blueprint('main', __name__)
app.config['SESSION_PERMANENT'] = False
babel = Babel(app)

@bp.before_app_request
def detect_lang():
    lang = request.args.get('lang')
    if lang in ['it', 'en', 'ar']:
        session['lang'] = lang

from myapp.main import routes
