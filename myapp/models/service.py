from myapp import db

class Service(db.Model):
    __tablename__ = 'services'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text, nullable=False)
    category = db.Column(db.String(50))
    image_filename = db.Column(db.String(200))

    def __repr__(self):
        return f'<Service {self.title}>'
