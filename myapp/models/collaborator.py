from myapp.extensions import db

class Collaborator(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    category = db.Column(db.String(50))
    name = db.Column(db.String(100))
    description = db.Column(db.Text)
    image_filename = db.Column(db.String(255))
