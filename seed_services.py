# myapp/seed_services.py

from myapp import create_app, db
from myapp.models import Service

app = create_app()

with app.app_context():
    # Cancella tutto (opzionale)
    Service.query.delete()
    db.session.commit()

    servizi = [
        {
            "title": "Location da sogno",
            "description": "Scopri le migliori location per il tuo matrimonio, tra ville, castelli e spiagge incantate.",
            "category": "Location",
            "image_filename": "location1.jpg"
        },
        {
            "title": "Catering gourmet",
            "description": "Menu personalizzati per soddisfare ogni palato con ingredienti freschi e stagionali.",
            "category": "Catering",
            "image_filename": "catering1.jpg"
        },
        {
            "title": "Decorazioni floreali",
            "description": "Allestimenti eleganti e su misura con fiori freschi e composizioni creative.",
            "category": "Allestimenti",
            "image_filename": "flowers1.jpg"
        },
        {
            "title": "Fotografia professionale",
            "description": "Servizi fotografici per catturare ogni momento del tuo giorno speciale.",
            "category": "Fotografia",
            "image_filename": "photo1.jpg"
        },
        {
            "title": "Musica e intrattenimento",
            "description": "DJ e band dal vivo per animare la tua festa fino a tarda notte.",
            "category": "Intrattenimento",
            "image_filename": "music1.jpg"
        }
    ]

    for s in servizi:
        servizio = Service(**s)
        db.session.add(servizio)
    db.session.commit()

    print("Servizi seedati con successo.")
