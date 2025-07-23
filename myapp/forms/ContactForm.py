from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Optional
from flask_babel import lazy_gettext as _

class ContactForm(FlaskForm):
    name = StringField(_('Nome'), validators=[DataRequired()])
    email = StringField(_('Email'), validators=[DataRequired(), Email()])
    phone = StringField(_('Telefono'), validators=[Optional()])
    subject = StringField(_('Oggetto'), validators=[DataRequired()])
    message = TextAreaField(_('Messaggio'), validators=[DataRequired()])
    recaptchaToken = StringField(_('Token'), validators=[DataRequired()])
    submit = SubmitField(_('Invia'))
