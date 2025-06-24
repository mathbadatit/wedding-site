from app import app, db, User

with app.app_context():
    db.create_all()
    if not User.query.filter_by(username='admin').first():
        admin = User(username='admin', password='admin')
        db.session.add(admin)
        db.session.commit()
        print("Admin creato con username 'admin' e password 'admin'.")
    else:
        print("Admin già presente nel database.")
