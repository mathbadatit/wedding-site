from myapp import create_app, db
from myapp.models import User
from werkzeug.security import generate_password_hash

app = create_app()

with app.app_context():
    db.create_all()
    admin_email = "nkh3771@gmaul.com"
    admin_password = "123admin"
    if not User.query.filter_by(email=admin_email).first():
        user = User(
            email=admin_email,
            is_admin=True
        )
        user.set_password(admin_password)  # Usa il metodo del modello per hashare la password
        db.session.add(user)
        db.session.commit()
        print(f"✅ Admin creato: {admin_email} / {admin_password}")
    else:
        print("⚠️ Admin esiste già.")
