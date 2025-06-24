from app import app, db, User
from getpass import getpass

def create_admin():
    with app.app_context():
        username = input("Username admin: ")
        password = getpass("Password admin: ")
        if User.query.filter_by(username=username).first():
            print("Utente già esistente.")
            return
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        print("Admin creato con successo.")

if __name__ == '__main__':
    create_admin()
