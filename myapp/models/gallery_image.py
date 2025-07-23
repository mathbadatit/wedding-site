from myapp.extensions import db

class GalleryImage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    filename = db.Column(db.String(255), nullable=False)
    order = db.Column(db.Integer, default=0)
    alt_text = db.Column(db.String(255), nullable=True)
