from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, DecimalField
from wtforms.validators import DataRequired, Email, Optional
from flask_babel import lazy_gettext as _

class BookingForm(FlaskForm):
    customer_name = StringField(_('Nome'), validators=[DataRequired()])
    customer_email = StringField(_('Email'), validators=[DataRequired(), Email()])
    customer_phone = StringField(_('Telefono'), validators=[Optional()])
    location = StringField(_('Location'), validators=[Optional()])
    budget = DecimalField(_('Budget'), validators=[Optional()])
    message = TextAreaField(_('Messaggio'), validators=[Optional()])
    recaptchaToken = StringField(_('Token'), validators=[DataRequired()])  # 👈 Da aggiungere
    submit = SubmitField(_('Prenota'))
