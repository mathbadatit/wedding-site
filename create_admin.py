from app import db, User

db.create_all()

# Crea admin con username admin e password admin123
if not User.query.filter_by(username='admin').first():
    admin = User(username='admin')
    admin.set_password('admin123')
    db.session.add(admin)
    db.session.commit()
    print('Admin creato.')
else:
    print('Admin già esistente.')
