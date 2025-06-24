from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel, _
from flask_mail import Mail, Message
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_migrate import Migrate
from werkzeug.security import generate_password_hash, check_password_hash
import os, requests
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-secret')
app.config['BABEL_DEFAULT_LOCALE'] = os.environ.get('BABEL_DEFAULT_LOCALE', 'it')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(app.instance_path, 'booking.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Mail config
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = app.config['MAIL_USERNAME']

mail = Mail(app)
babel = Babel(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

RECAPTCHA_SECRET_KEY = os.environ.get('RECAPTCHA_SECRET_KEY')

# MODELS
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)

    def set_password(self, pw): self.password_hash = generate_password_hash(pw)
    def check_password(self, pw): return check_password_hash(self.password_hash, pw)

# ... altri model (Service, Booking, GalleryImage) ...

@login_manager.user_loader
def load_user(user_id): return User.query.get(int(user_id))

# ROTTE pubbliche: public_home, gallery, login/logout, dashboard, add_service, upload_image ...

@app.route('/booking', methods=['GET','POST'])
def booking():
    if request.method == 'POST':
        data = request.json
        token = data.get('recaptchaToken')
        rec = requests.post('https://www.google.com/recaptcha/api/siteverify',
            data={'secret': RECAPTCHA_SECRET_KEY, 'response': token}).json()
        if not rec.get('success') or rec.get('score',0) < 0.5:
            return jsonify({'success':False,'message':_('reCAPTCHA non superato')}),400
        if not data.get('nome') or not data.get('email') or not data.get('data'):
            return jsonify({'success':False,'message':_('Compila tutti i campi obbligatori')}),400
        new = Booking(nome=data['nome'], email=data['email'],
                      telefono=data.get('telefono',''),
                      data=data['data'], location=data.get('location',''),
                      budget=data.get('budget',''))
        db.session.add(new); db.session.commit()

        # Email all’admin
        msg_admin = Message(_('Nuova prenotazione ricevuta'),
            recipients=[app.config['MAIL_USERNAME']])
        msg_admin.body = f"Nuova prenotazione:\nNome: {new.nome}\n..."  # completo come prima
        mail.send(msg_admin)

        # Email al cliente + allegato (pdf esempio)
        msg_client = Message(_('Grazie per la tua prenotazione!'),
            recipients=[new.email])
        msg_client.body = _('Ciao {0},\n\nGrazie per averci contattato. Ti confermiamo la prenotazione il {1}.\n\nA presto!').format(new.nome, new.data)
        # allego static/brochure.pdf
        with open(os.path.join(app.root_path, 'static', 'brochure.pdf'), 'rb') as f:
            msg_client.attach('brochure.pdf', 'application/pdf', f.read())
        mail.send(msg_client)

        return jsonify({'success':True,'message':_('Prenotazione ricevuta!')})
    return render_template('booking.html', recaptcha_site_key=os.environ.get('RECAPTCHA_SITE_KEY'))

# Rotta contact AJAX + recaptcha simile, email gestione con conferma cliente

if __name__ == '__main__':
    app.run(debug=True)
