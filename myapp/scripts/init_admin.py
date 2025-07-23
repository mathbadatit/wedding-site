# myapp/scripts/init_admin.py

from myapp import create_app, db
from myapp.models import User
from werkzeug.security import generate_password_hash
import os

def init_admin():
    app = create_app()
    with app.app_context():
        db.create_all()

        admin_email = os.getenv('ADMIN_EMAIL', 'admin@example.com')
        admin_password = os.getenv('ADMIN_PASSWORD', 'admin123')

        admin = User.query.filter_by(email=admin_email).first()

        if admin:
            print(f"[INFO] Admin already exists: {admin_email}")
        else:
            new_admin = User(
                email=admin_email,
                password=generate_password_hash(admin_password),
                role='admin'
            )
            db.session.add(new_admin)
            db.session.commit()
            print(f"[SUCCESS] Admin created: {admin_email}")

if __name__ == "__main__":
    init_admin()
