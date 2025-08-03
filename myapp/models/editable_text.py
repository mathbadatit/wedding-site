from myapp import db

class EditableText(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    identifier = db.Column(db.String(64), unique=True, nullable=False)
    content = db.Column(db.Text, nullable=False)
    
    def __repr__(self):
        return f"<EditableText {self.identifier}>"
