from myapp import create_app, db
from myapp.models import Service, GalleryImage, Collaborator

# 1️⃣ Crea l'app Flask
app = create_app()

# 2️⃣ Lista di servizi da inserire (puoi aggiungerne quanti vuoi)
demo_services = [
    {
        "title_it": "Servizio Fotografico",
        "description_it": "Pacchetto completo foto e video",
        "title_en": "Photography Service",
        "description_en": "Full photo and video package",
        "title_ar": "خدمة التصوير",
        "description_ar": "باقة كاملة من الصور والفيديو"
    },
    {
        "title_it": "Servizio Catering",
        "description_it": "Catering di alta qualità per il tuo matrimonio",
        "title_en": "Catering Service",
        "description_en": "High-quality catering for your wedding",
        "title_ar": "خدمة تقديم الطعام",
        "description_ar": "خدمة تقديم طعام عالية الجودة لحفل زفافك"
    }
    # Aggiungi altre dict {} come queste per altri servizi
]

# 3️⃣ Lista di collaboratori
demo_collaborators = [
    Collaborator(
        name="Mario Rossi",
        category="Fotografo",
        description="Fotografo professionista specializzato in matrimoni",
        image_filename="mario.jpg"
    ),
    Collaborator(
        name="Giulia Bianchi",
        category="Wedding Planner",
        description="Organizzatrice di eventi specializzata in matrimoni",
        image_filename="giulia.jpg"
    )
    # Aggiungi altri Collaborator() come questi
]

# 4️⃣ Immagini Galleria
demo_gallery = [
    GalleryImage(
        filename="foto1.jpg",
        order=1,
        alt_text="Foto romantica sposi"
    ),
    GalleryImage(
        filename="foto2.jpg",
        order=2,
        alt_text="Torta nuziale"
    )
    # Aggiungi altre GalleryImage() come questi
]

# 5️⃣ Inserimento nel DB
with app.app_context():
    db.create_all()

    # Inserisci i servizi
    for s in demo_services:
        if not Service.query.filter_by(title_it=s["title_it"]).first():
            db.session.add(Service(**s))

    # Inserisci i collaboratori
    for c in demo_collaborators:
        if not Collaborator.query.filter_by(name=c.name).first():
            db.session.add(c)

    # Inserisci le immagini della galleria
    for g in demo_gallery:
        if not GalleryImage.query.filter_by(filename=g.filename).first():
            db.session.add(g)

    db.session.commit()
    print("✅ Tutto inserito correttamente nel database")
