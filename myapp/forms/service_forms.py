from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, URL

class ServiceForm(FlaskForm):
    title = StringField('Titolo', validators=[DataRequired()])
    description = TextAreaField('Descrizione', validators=[DataRequired()])
    image_url = StringField('URL immagine', validators=[DataRequired(), URL()])
    submit = SubmitField('Salva')
