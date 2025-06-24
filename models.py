class EmailLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(255))
    recipient = db.Column(db.String(120))
    body = db.Column(db.Text)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
