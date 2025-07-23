from flask import render_template, request, session, redirect, url_for
from flask_login import current_user
from myapp.models import Service, GalleryImage, Collaborator, ContactMessage
from myapp.main import bp  # Usa il blueprint definito in __init__.py


@bp.route('/')
def home():
    services = Service.query.all()
    images = GalleryImage.query.order_by(GalleryImage.order).all()
    collaborators = Collaborator.query.all()
    unread_count = ContactMessage.query.filter_by(read=False).count() if current_user.is_authenticated else 0
    return render_template('home.html', services=services, images=images, collaborators=collaborators, unread_count=unread_count)


@bp.route('/about')
def about():
    return render_template('about.html')


@bp.route('/services')
def services():
    lang = session.get('lang', 'it')
    all_services = Service.query.all()
    services_data = []
    for s in all_services:
        title = getattr(s, f"title_{lang}", s.title_it)
        description = getattr(s, f"description_{lang}", s.description_it)
        services_data.append({'title': title, 'description': description})
    return render_template('services.html', services=services_data)


@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')


@bp.route('/setlang/<lang>')
def set_language(lang):
    session['lang'] = lang
    return redirect(request.referrer or url_for('main.home'))


@bp.route('/set_language/<lang>')
def set_language(lang):
    session['lang'] = lang
    return redirect(request.referrer or url_for('main.home'))
