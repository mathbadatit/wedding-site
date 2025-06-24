from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_babel import Babel, _
from flask_mail import Mail, Message
from dotenv import load_dotenv
import os
import requests

load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret')
app.config['BABEL_DEFAULT_LOCALE'] = os.environ.get('BABEL_DEFAULT_LOCALE', 'it')

# Mail config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.environ.get('MAIL_USERNAME')

mail = Mail(app)
babel = Babel(app)

# reCAPTCHA config
RECAPTCHA_SECRET_KEY = os.environ.get('RECAPTCHA_SECRET_KEY')

# --- ROTTE ---

@app.route('/')
def public_home():
    return render_template('home.html')

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        data = request.json
        token = data.get('recaptchaToken')

        recaptcha_response = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={
                'secret': RECAPTCHA_SECRET_KEY,
                'response': token
            }
        )
        result = recaptcha_response.json()
        if not result.get('success') or result.get('score', 0) < 0.5:
            return jsonify({'success': False, 'message': _('reCAPTCHA non superato')}), 400

        # Validazione base
        if not data.get('nome') or not data.get('email') or not data.get('data'):
            return jsonify({'success': False, 'message': _('Compila tutti i campi obbligatori')}), 400

        # Salva in DB
        new = Booking(
            nome=data['nome'],
            email=data['email'],
            telefono=data.get('telefono', ''),
            data=data['data'],
            location=data.get('location', ''),
            budget=data.get('budget', '')
        )
        db.session.add(new)
        db.session.commit()

        # Email admin
        msg_admin = Message(_('Nuova prenotazione ricevuta'),
                      recipients=[app.config['MAIL_USERNAME']])
        msg_admin.body = f"""
        Nuova prenotazione:

        Nome: {new.nome}
        Email: {new.email}
        Telefono: {new.telefono}
        Data: {new.data}
        Location: {new.location}
        Budget: {new.budget}
        """

        # Se vuoi allegare un file (opzionale)
        # msg_admin.attach("booking.pdf", "application/pdf", pdf_data)

        mail.send(msg_admin)

        # Email al cliente
        msg_client = Message(_('Grazie per la prenotazione!'),
                             recipients=[new.email])
        msg_client.body = f"Ciao {new.nome}, grazie per averci contattato! Ti risponderemo presto."
        mail.send(msg_client)
# dopo mail.send(msg) al cliente
# Invierà una email anche al cliente
reply = Message(_('Grazie per la tua prenotazione!'),
                recipients=[new.email])
reply.body = _('Ciao {0},\n\nGrazie per averci contattato. Ti confermiamo la prenotazione il {1}.\n\nA presto!').format(new.nome, new.data)
mail.send(reply)

        return jsonify({'success': True, 'message': _('Prenotazione ricevuta!')})

    return render_template('booking.html', recaptcha_site_key=os.environ.get('RECAPTCHA_SITE_KEY'))

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.json
        token = data.get('recaptchaToken')

        recaptcha_response = requests.post(
            'https://www.google.com/recaptcha/api/siteverify',
            data={'secret': RECAPTCHA_SECRET_KEY, 'response': token}
        )
        result = recaptcha_response.json()
        if not result.get('success') or result.get('score', 0) < 0.5:
            return jsonify({'success': False, 'message': _('reCAPTCHA non superato')}), 400

        if not data.get('nome') or not data.get('email') or not data.get('messaggio'):
            return jsonify({'success': False, 'message': _('Compila tutti i campi obbligatori')}), 400

        # Email a te
        msg_admin = Message(_('Nuovo messaggio da contatto'),
            recipients=[app.config['MAIL_USERNAME']])
        msg_admin.body = f"""Messaggio da: {data['nome']} <{data['email']}>
{data['messaggio']}"""
        mail.send(msg_admin)

        # Email di conferma al cliente
        msg_client = Message(_('Grazie per averci contattato!'),
            recipients=[data['email']])
        msg_client.body = _('Abbiamo ricevuto il tuo messaggio e ti risponderemo presto.')
        mail.send(msg_client)

        return jsonify({'success': True, 'message': _('Messaggio inviato, grazie!')})

    return render_template('contact.html', recaptcha_site_key=os.environ.get('RECAPTCHA_SITE_KEY'))
