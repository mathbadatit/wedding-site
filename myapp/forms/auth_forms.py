from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from flask_babel import lazy_gettext as _

class LoginForm(FlaskForm):
    username = StringField(_('Username'), validators=[DataRequired()])
    password = PasswordField(_('Password'), validators=[DataRequired()])
    submit = SubmitField(_('Login'))

class RegisterForm(FlaskForm):
    email = StringField(_('Email'), validators=[DataRequired(), Email()])
    username = StringField(_('Username'), validators=[DataRequired()])
    password = PasswordField(_('Password'), validators=[DataRequired()])
    submit = SubmitField(_('Registrati'))
