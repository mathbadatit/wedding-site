from flask import render_template, redirect, url_for, flash, request
from flask_login import login_user, logout_user, login_required
from werkzeug.security import check_password_hash
from myapp.models.user import User
from myapp.auth.forms import LoginForm
from myapp.auth import bp

@bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and check_password_hash(user.password_hash, form.password.data):
            login_user(user)
            return redirect(url_for('admin.dashboard'))
        flash('Credenziali non valide', 'danger')
    return render_template('auth/admin_login.html', form=form)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('Logout effettuato', 'success')
    return redirect(url_for('auth.login'))
