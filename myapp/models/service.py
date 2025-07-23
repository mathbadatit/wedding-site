from myapp.extensions import db
class Service(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title_it = db.Column(db.String(200), nullable=False)  # Italiano obbligatorio
    title_en = db.Column(db.String(200), nullable=True)   # Inglese opzionale
    title_ar = db.Column(db.String(200), nullable=True)   # Arabo opzionale
    description_it = db.Column(db.Text, nullable=False)
    description_en = db.Column(db.Text, nullable=False)
    description_ar = db.Column(db.Text, nullable=False)
