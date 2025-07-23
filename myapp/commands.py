import click
from flask.cli import with_appcontext
from myapp.extensions import db
from myapp.models import AdminUser, Service, GalleryImage, Collaborator
from werkzeug.security import generate_password_hash
import os
import shutil
import json

@click.command('init-db')
@with_appcontext
def init_db_command():
    db.create_all()
    click.echo('✅ Database inizializzato.')

@click.command('reset-db')
@with_appcontext
def reset_db_command():
    db.drop_all()
    db.create_all()
    click.echo('✅ Database resettato.')

@click.command('migrate-db')
@with_appcontext
def migrate_db_command():
    os.system('flask db migrate -m "Auto migration" && flask db upgrade')
    click.echo('✅ Migrazioni completate.')

@click.command('create-admin')
@click.option('--username', prompt=True)
@click.option('--email', prompt=True)
@click.option('--password', prompt=True, hide_input=True, confirmation_prompt=True)
@with_appcontext
def create_admin(username, email, password):
    if AdminUser.query.filter_by(username=username).first():
        click.echo(f'ℹ️ Admin {username} già esistente.')
    else:
        admin = AdminUser(username=username, email=email, role='admin')
        admin.password_hash = generate_password_hash(password)
        db.session.add(admin)
        db.session.commit()
        click.echo(f'✅ Admin {username} creato.')

@click.command('create-admins')
@click.argument('json_file')
@with_appcontext
def create_admins(json_file):
    try:
        with open(json_file, 'r', encoding='utf-8') as f:
            admins = json.load(f)
    except Exception as e:
        click.echo(f'❗ Errore nel file JSON: {e}')
        return

    for adm in admins:
        username = adm.get('username')
        email = adm.get('email')
        password = adm.get('password')
        if not username or not email or not password:
            click.echo(f'❗ Dati mancanti per admin: {adm}')
            continue
        if AdminUser.query.filter_by(username=username).first():
            click.echo(f'ℹ️ Admin {username} già esistente.')
        else:
            new_admin = AdminUser(username=username, email=email, role='admin')
            new_admin.password_hash = generate_password_hash(password)
            db.session.add(new_admin)
            click.echo(f'✅ Creato admin {username}')
    db.session.commit()
    click.echo('✅ Inserimento completato.')

@click.command('clear-uploads')
@with_appcontext
def clear_uploads_command():
    folder = os.path.join(os.getcwd(), 'instance', 'uploads')
    if os.path.exists(folder):
        shutil.rmtree(folder)
        os.makedirs(folder)
        click.echo('✅ Uploads svuotati.')
    else:
        click.echo('ℹ️ Cartella uploads non trovata.')

@click.command('seed-demo')
@with_appcontext
def seed_demo():
    if Service.query.first():
        click.echo('ℹ️ Dati demo già presenti.')
        return
    s = Service(
        title_it='Servizio Demo',
        description_it='Descrizione Demo IT',
        title_en='Demo Service',
        description_en='Demo Description EN',
        title_ar='خدمة تجريبية',
        description_ar='الوصف التجريبي'
    )
    g = GalleryImage(filename='prova.jpg', order=1, alt_text='Immagine Demo')
    c = Collaborator(name='Collaboratore Demo', category='Fotografo', description='Descrizione Demo', image_filename='prova.jpg')
    db.session.add_all([s, g, c])
    db.session.commit()
    click.echo('✅ Dati demo inseriti.')

def register_commands(app):
    app.cli.add_command(init_db_command)
    app.cli.add_command(reset_db_command)
    app.cli.add_command(migrate_db_command)
    app.cli.add_command(create_admin)
    app.cli.add_command(create_admins)
    app.cli.add_command(clear_uploads_command)
    app.cli.add_command(seed_demo)
