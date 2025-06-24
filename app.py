from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_babel import Babel, _
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
import os
import requests

app = Flask(__name__)

# Config .env
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret')
app.config['BABEL_DEFAULT_LOCALE'] = os.environ.get('BABEL_DEFAULT_LOCALE', 'it')

# DB config (aggiungi se manca)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'booking.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

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

# Modello Booking esempio
class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    telefono = db.Column(db.String(20))
    data = db.Column(db.String(20))
    location = db.Column(db.String(150))
    budget = db.Column(db.String(50))

# --- Booking route (AJAX + reCAPTCHA)
@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        data = request.json  # AJAX manda JSON
        token = data.get('recaptchaToken')

        # Verifica reCAPTCHA
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

        # Validazioni basilari
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

        # Invia email
        msg = Message(_('Nuova prenotazione ricevuta'),
                      recipients=[app.config['MAIL_USERNAME']])
        msg.body = f"""
Nuova prenotazione:

Nome: {new.nome}
Email: {new.email}
Telefono: {new.telefono}
Data: {new.data}
Location: {new.location}
Budget: {new.budget}
"""
        mail.send(msg)

        return jsonify({'success': True, 'message': _('Prenotazione ricevuta!')})

    # GET: mostra form
    return render_template('booking.html', recaptcha_site_key=os.environ.get('RECAPTCHA_SITE_KEY'))


# --- Contact route (simile con AJAX e reCAPTCHA)
@app.route('/contact', methods=['GET', 'POST'])
def contact():
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

        if not data.get('nome') or not data.get('email') or not data.get('messaggio'):
            return jsonify({'success': False, 'message': _('Compila tutti i campi obbligatori')}), 400

        # Invia email contatto
        msg = Message(_('Nuovo messaggio da contatto'),
                      recipients=[app.config['MAIL_USERNAME']])
        msg.body = f"""
Messaggio da: {data['nome']} <{data['email']}>

Messaggio:
{data['messaggio']}
"""
        mail.send(msg)

        return jsonify({'success': True, 'message': _('Messaggio inviato, grazie!')})

    return render_template('contact.html', recaptcha_site_key=os.environ.get('RECAPTCHA_SITE_KEY'))

if __name__ == '__main__':
    app.run(debug=True)
