from myapp.extensions import db

class EditableText(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(255), unique=True, nullable=False)
    content = db.Column(db.Text)
