from myapp.extensions import db
from datetime import datetime

class Booking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    customer_name = db.Column(db.String(100), nullable=False)
    customer_email = db.Column(db.String(120), nullable=False)
    customer_phone = db.Column(db.String(50))
    location = db.Column(db.String(200))
    budget = db.Column(db.String(50))
    message = db.Column(db.Text)
    date = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default="In attesa")
