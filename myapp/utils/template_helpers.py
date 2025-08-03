# myapp/template_helpers.py
from flask import url_for

def login_url():
    return url_for('auth.login')

def home_url():
    return url_for('main.home')
