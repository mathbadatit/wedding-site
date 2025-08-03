from myapp import create_app, db
from myapp.models import Service

app = create_app()
app.app_context().push()

# Seed dati
services = [
    Service(title='Location esclusiva', description='Ville e castelli da sogno.', category='Location', image_filename='location.jpg'),
    Service(title='Catering gourmet', description='Piatti raffinati e personalizzati.', category='Catering', image_filename='catering.jpg'),
    Service(title='Allestimento floreale', description='Decorazioni eleganti e tematiche.', category='Allestimenti', image_filename='flowers.jpg'),
]

db.session.bulk_save_objects(services)
db.session.commit()
print("✅ Dati di esempio inseriti.")
