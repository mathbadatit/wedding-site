from datetime import datetime
from myapp.extensions import db

class GalleryImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    alt_text = db.Column(db.String(255), nullable=True)
    upload_date = db.Column(db.DateTime, default=datetime.utcnow)
    order = db.Column(db.Integer, nullable=True)  # Questo campo serve per ordinare le immagini
