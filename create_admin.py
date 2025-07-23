from myapp.extensions import db, create_app
from myapp.models import User
from werkzeug.security import generate_password_hash

myapp = create_app()

def create_admin(username, password):
    with myapp.app_context():
        if User.query.filter_by(username=username).first():
            print("Utente già esistente.")
        else:
            hashed_pw = generate_password_hash(password)
            new_admin = User(username=username, password_hash=hashed_pw)
            db.session.add(new_admin)
            db.session.commit()
            print(f"Admin '{username}' creato con successo.")

if __name__ == "__main__":
    create_admin("admin", "admin123")
