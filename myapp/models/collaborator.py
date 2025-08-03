from myapp.extensions import db

class Collaborator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=True)  # ✅ AGGIUNGI QUESTO
    bio = db.Column(db.Text, nullable=True)
    image_filename = db.Column(db.String(255), nullable=True)
