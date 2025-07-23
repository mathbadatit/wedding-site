from functools import wraps
from flask import flash, redirect, url_for
from flask_login import current_user
from flask_babel import _
from myapp.models import AdminLog
from myapp.extensions import db

def admin_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if not current_user.is_authenticated or current_user.role != 'admin':
            flash(_('Accesso non autorizzato'), 'danger')
            return redirect(url_for('admin.login'))
        return f(*args, **kwargs)
    return decorated_function

def log_admin_action(action):
    if current_user.is_authenticated:
        log = AdminLog(user_id=current_user.id, action=action)
        db.session.add(log)
        db.session.commit()
