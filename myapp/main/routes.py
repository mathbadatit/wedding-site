from flask import render_template, request, session, redirect, url_for, current_app
from flask_login import current_user
from myapp.models import Service, GalleryImage, Collaborator, ContactMessage
from myapp.main import bp  # blueprint definito in __init__.py

# Home Page
@bp.route('/')
def home():
    lang = session.get('lang', 'it')  # Lingua corrente

    # Dati Servizi multilingua
    services_data = []
    for s in Service.query.all():
        title = getattr(s, f"title_{lang}", s.title_it)
        description = getattr(s, f"description_{lang}", s.description_it)
        services_data.append({'title': title, 'description': description})

    # Galleria immagini ordinata
    images = GalleryImage.query.order_by(GalleryImage.order).all()

    # Collaboratori
    collaborators = Collaborator.query.all()

    # Messaggi non letti (se loggato)
    unread_count = ContactMessage.query.filter_by(read=False).count() if current_user.is_authenticated else 0

    return render_template(
        'home.html',
        services=services_data,
        images=images,
        collaborators=collaborators,
        unread_count=unread_count
    )

# Pagina About
@bp.route('/about')
def about():
    return render_template('about.html')

# Pagina Servizi (separata da home)
@bp.route('/services')
def services():
    lang = session.get('lang', 'it')
    services_data = []
    for s in Service.query.all():
        title = getattr(s, f"title_{lang}", s.title_it) or "N/A"
        description = getattr(s, f"description_{lang}", s.description_it) or "N/A"
        services_data.append({'title': title, 'description': description})
    return render_template('services.html', services=services_data)

# Pagina Contatti (placeholder, va completata con form)
@bp.route('/contact', methods=['GET', 'POST'])
def contact():
    return render_template('contact.html')

# Cambia lingua
@bp.route('/setlang/<lang_code>')
def setlang(lang_code):
    session['lang'] = lang_code
    return redirect(request.referrer or url_for('main.home'))
