from flask import Blueprint, render_template, request, flash, redirect, url_for
from .forms import ContactForm
from .models import ContactMessage
from myapp.extensions import db  # ✅ giusto così
from flask_babel import gettext as _
from myapp.utils import verify_recaptcha
from myapp.email_utils import send_email

contact_bp = Blueprint('contact', __name__)

@contact_bp.route('/contact', methods=['GET', 'POST'])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        if not verify_recaptcha(form.recaptchaToken.data):
            flash(_('Verifica reCAPTCHA fallita. Riprova.'), 'danger')
            return redirect(url_for('contact.contact'))

        new_msg = ContactMessage(
            name=form.name.data,
            email=form.email.data,
            phone=form.phone.data,
            subject=form.subject.data,
            message=form.message.data
        )
        db.session.add(new_msg)
        db.session.commit()

        try:
            send_email(
                subject="📥 Nuovo messaggio da contatto",
                recipients=['tuamail@tuo.it'],
                html_body=render_template('email/contact_notification.html', message=new_msg)
            )
            flash(_('Grazie per averci contattato! Ti risponderemo al più presto.'), 'success')
        except Exception as e:
            flash(_('Errore nell\'invio della mail, ma messaggio salvato.'), 'warning')
        return redirect(url_for('contact.contact'))

    return render_template('contact.html', form=form)
