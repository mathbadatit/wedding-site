from flask_wtf import FlaskForm, RecaptchaField
from wtforms import (
    StringField, PasswordField, TextAreaField, FileField,
    SelectField, SubmitField, BooleanField, DecimalField
)
from wtforms.validators import DataRequired, Length, Email, ValidationError, Optional
from flask_wtf.file import FileAllowed, FileRequired
from flask_babel import lazy_gettext as _l
from .models import Booking, AdminUser

# Validator personalizzato per budget
def validate_budget_value(form, field):
    if field.data is None:
        raise ValidationError(_l("Inserisci un numero valido."))
    try:
        value = float(field.data)
    except (ValueError, TypeError):
        raise ValidationError(_l("Inserisci un numero valido."))
    if value < 500:
        raise ValidationError(_l("Il budget minimo è 500€."))

class BaseForm(FlaskForm):
    class Meta:
        csrf = True  # Mantieni csrf attivo, disattiva solo per test

class LoginForm(BaseForm):
    username = StringField(
        _l('Nome Utente'),
        validators=[DataRequired(_l('Campo obbligatorio'))],
        render_kw={"placeholder": _l("Inserisci il tuo nome utente"), "autocomplete": "username", "aria-label": _l("Nome Utente")}
    )
    password = PasswordField(
        _l('Password'),
        validators=[DataRequired(_l('Campo obbligatorio'))],
        render_kw={"placeholder": _l("Inserisci la tua password"), "autocomplete": "current-password", "aria-label": _l("Password")}
    )
    recaptcha = RecaptchaField()
    submit = SubmitField(_l('Accedi'), render_kw={"aria-label": _l("Accedi")})

class ServiceForm(BaseForm):
    title_it = StringField(
        _l('Titolo IT'),
        validators=[DataRequired(_l('Campo obbligatorio')), Length(max=150)],
        render_kw={"placeholder": _l("Inserisci il titolo in italiano"), "aria-label": _l("Titolo in Italiano")}
    )
    title_en = StringField(
        _l('Titolo EN'),
        validators=[DataRequired(_l('Campo obbligatorio')), Length(max=150)],
        render_kw={"placeholder": _l("Enter title in English"), "aria-label": _l("Title in English")}
    )
    title_ar = StringField(
        _l('Titolo AR'),
        validators=[DataRequired(_l('Campo obbligatorio')), Length(max=150)],
        render_kw={"placeholder": _l("أدخل العنوان باللغة العربية"), "aria-label": _l("Title in Arabic")}
    )
    description_it = TextAreaField(
        _l('Descrizione IT'),
        validators=[DataRequired(_l('Campo obbligatorio'))],
        render_kw={"placeholder": _l("Scrivi la descrizione in italiano"), "rows": 4, "aria-label": _l("Descrizione in Italiano")}
    )
    description_en = TextAreaField(
        _l('Descrizione EN'),
        validators=[DataRequired(_l('Campo obbligatorio'))],
        render_kw={"placeholder": _l("Write the description in English"), "rows": 4, "aria-label": _l("Description in English")}
    )
    description_ar = TextAreaField(
        _l('Descrizione AR'),
        validators=[DataRequired(_l('Campo obbligatorio'))],
        render_kw={"placeholder": _l("اكتب الوصف باللغة العربية"), "rows": 4, "aria-label": _l("Description in Arabic")}
    )
    submit = SubmitField(_l('Salva'))

class UserForm(BaseForm):
    username = StringField(
        _l('Nome Utente'),
        validators=[DataRequired(_l('Campo obbligatorio'))],
        render_kw={"placeholder": _l("Inserisci il nome utente"), "aria-label": _l("Nome Utente")}
    )
    password = PasswordField(
        _l('Password'),
        render_kw={"placeholder": _l("Lascia vuoto per non modificare"), "aria-label": _l("Password")}
    )
    role = SelectField(
        _l('Ruolo'),
        choices=[
            ('admin', _l('Admin')),
            ('editor', _l('Editor'))
        ],
        validators=[DataRequired(_l('Campo obbligatorio'))],
        render_kw={"aria-label": _l("Ruolo")}
    )
    submit = SubmitField(_l('Salva'))

class CollaboratorForm(BaseForm):
    category = StringField(
        _l('Categoria'),
        validators=[DataRequired(_l('Campo obbligatorio'))],
        render_kw={"placeholder": _l("Inserisci la categoria"), "aria-label": _l("Categoria")}
    )
    name = StringField(
        _l('Nome'),
        validators=[DataRequired(_l('Campo obbligatorio'))],
        render_kw={"placeholder": _l("Inserisci il nome del collaboratore"), "aria-label": _l("Nome")}
    )
    description = TextAreaField(
        _l('Descrizione'),
        validators=[DataRequired(_l('Campo obbligatorio'))],
        render_kw={"placeholder": _l("Scrivi la descrizione"), "rows": 4, "aria-label": _l("Descrizione")}
    )
    image = FileField(
        _l('Immagine'),
        validators=[FileAllowed(['jpg', 'jpeg', 'png', 'svg'], _l('Solo immagini'))],
        render_kw={"aria-label": _l("Immagine")}
    )
    submit = SubmitField(_l('Salva'))

class GalleryUploadForm(BaseForm):
    image = FileField(
        _l('Immagine'),
        validators=[
            FileRequired(_l('Seleziona un\'immagine')),
            FileAllowed(['jpg', 'jpeg', 'png', 'svg'], _l('Solo immagini'))
        ],
        render_kw={"aria-label": _l("Immagine")}
    )
    submit = SubmitField(_l('Carica'))

class BookingForm(BaseForm):
    name = StringField(
        _l('Nome'),
        validators=[DataRequired(_l('Campo obbligatorio'))],
        render_kw={"placeholder": _l("Il tuo nome completo"), "autocomplete": "name", "aria-label": _l("Nome")}
    )
    email = StringField(
        _l('Email'),
        validators=[DataRequired(_l('Campo obbligatorio')), Email(_l('Email non valida'))],
        render_kw={"placeholder": _l("La tua email"), "autocomplete": "email", "aria-label": _l("Email")}
    )
    phone = StringField(
        _l('Telefono'),
        validators=[DataRequired(_l('Campo obbligatorio')), Length(max=20)],
        render_kw={"placeholder": _l("Il tuo numero di telefono"), "autocomplete": "tel", "aria-label": _l("Telefono")}
    )
    location = StringField(
        _l('Luogo desiderato'),
        validators=[DataRequired(_l('Campo obbligatorio'))],
        render_kw={"placeholder": _l("Es. Roma, Milano"), "aria-label": _l("Luogo desiderato")}
    )
    city = SelectField(
        _l('Città/Regione'),
        choices=[
            ('roma', _l('Roma')),
            ('milano', _l('Milano')),
            ('napoli', _l('Napoli')),
            ('altro', _l('Altro'))
        ],
        validators=[DataRequired(_l('Seleziona una città/regione'))],
        render_kw={"aria-label": _l("Città o Regione")}
    )
    budget = DecimalField(
        _l('Budget (€)'),
        validators=[Optional(), validate_budget_value],
        places=2,
        render_kw={"placeholder": _l("Il tuo budget indicativo"), "step": "0.01", "aria-label": _l("Budget")}
    )
    submit = SubmitField(_l('Invia'))

class ContactForm(BaseForm):
    name = StringField(
        _l('Nome'),
        validators=[DataRequired()],
        render_kw={"placeholder": _l("Il tuo nome completo"), "autocomplete": "name", "aria-label": _l("Nome")}
    )
    email = StringField(
        _l('Email'),
        validators=[DataRequired(), Email()],
        render_kw={"placeholder": _l("La tua email"), "autocomplete": "email", "aria-label": _l("Email")}
    )
    phone = StringField(
        _l('Telefono'),
        validators=[Length(max=20), Optional()],
        render_kw={"placeholder": _l("Il tuo numero di telefono (opzionale)"), "autocomplete": "tel", "aria-label": _l("Telefono")}
    )
    subject = StringField(
        _l('Oggetto'),
        validators=[DataRequired()],
        render_kw={"placeholder": _l("Oggetto del messaggio"), "aria-label": _l("Oggetto")}
    )
    reason = SelectField(
        _l('Motivo del contatto'),
        choices=[
            ('info', _l('Richiesta informazioni')),
            ('collab', _l('Proposta collaborazione')),
            ('altro', _l('Altro'))
        ],
        validators=[DataRequired()],
        render_kw={"aria-label": _l("Motivo del contatto")}
    )
    message = TextAreaField(
        _l('Messaggio'),
        validators=[DataRequired()],
        render_kw={"placeholder": _l("Scrivi il tuo messaggio..."), "rows": 6, "aria-label": _l("Messaggio")}
    )
    gdpr = BooleanField(
        _l('Accetto il trattamento dei dati personali (GDPR)'),
        validators=[DataRequired()]
    )
    recaptcha = RecaptchaField()
    submit = SubmitField(_l('Invia messaggio'))
