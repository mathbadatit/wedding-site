from flask import Blueprint, request, session

bp = Blueprint('main', __name__)

@bp.before_app_request
def detect_lang():
    lang = request.args.get('lang')
    if lang in ['it', 'en', 'ar']:
        session['lang'] = lang

from myapp.main import routes
