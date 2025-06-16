from flask import Flask, render_template, request, redirect, url_for
from flask_babel import Babel, _
import sqlite3
import os

app = Flask(__name__)
print("✅ Sto eseguendo il file GIUSTO da Desktop!")
app.config['SECRET_KEY'] = 'secret-key'
app.config['BABEL_DEFAULT_LOCALE'] = 'it'
babel = Babel(app)

DATABASE = 'booking.db'

def get_db_connection():
    conn = sqlite3.connect(DATABASE)
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/services')
def services():
    return render_template('services.html')

@app.route('/booking', methods=['GET', 'POST'])
def booking():
    if request.method == 'POST':
        nome = request.form['nome']
        email = request.form['email']
        telefono = request.form.get('telefono')
        data = request.form['data']
        location = request.form.get('location')
        budget = request.form.get('budget')

        conn = get_db_connection()
        conn.execute('INSERT INTO bookings (nome, email, telefono, data, location, budget) VALUES (?, ?, ?, ?, ?, ?)',
                     (nome, email, telefono, data, location, budget))
        conn.commit()
        conn.close()
        return redirect(url_for('thankyou'))
    return render_template('booking.html')

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

if __name__ == '__main__':
    if not os.path.exists(DATABASE):
        conn = sqlite3.connect(DATABASE)
        conn.execute('''
            CREATE TABLE bookings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                email TEXT NOT NULL,
                telefono TEXT,
                data TEXT,
                location TEXT,
                budget TEXT
            )
        ''')
        conn.commit()
        conn.close()
    app.run(debug=True)
