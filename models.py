from datetime import datetime
from app import db  # Assumendo che 'db' sia l'istanza di SQLAlchemy creata in app.py

class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<Service {self.title}>'

class GalleryImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(200), nullable=False)
    caption = db.Column(db.String(200))

    def __repr__(self):
        return f'<GalleryImage {self.caption or self.filename}>'
