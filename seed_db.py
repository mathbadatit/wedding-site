from myapp import create_app, db
from myapp.models import Service, GalleryImage, Collaborator, EditableText
import os

app = create_app()

with app.app_context():
    db.create_all()

    # ➤ Servizi multilingua
    services = [
        Service(
            title_it="Fotografia Matrimoniale",
            description_it="Servizio fotografico completo durante tutto l'evento.",
            title_en="Wedding Photography",
            description_en="Complete photo coverage during your special day.",
            title_ar="تصوير الزفاف",
            description_ar="تغطية تصوير كاملة ليوم الزفاف الخاص بك."
        ),
        Service(
            title_it="Video Professionale",
            description_it="Riprese video in alta qualità per ricordare ogni momento.",
            title_en="Professional Video",
            description_en="High-quality video shooting to capture every moment.",
            title_ar="فيديو احترافي",
            description_ar="تسجيل فيديو عالي الجودة لكل اللحظات المهمة."
        ),
        Service(
            title_it="Location e Allestimenti",
            description_it="Consulenza su location da sogno e decorazioni raffinate.",
            title_en="Venue & Decoration",
            description_en="Advice on dream locations and refined decoration.",
            title_ar="المكان والديكور",
            description_ar="نصائح حول أماكن الزفاف الفاخرة والديكورات الراقية."
        )
    ]
    db.session.add_all(services)

    # ➤ Immagini galleria presenti nella cartella 'static/uploads'
    upload_folder = os.path.join(app.root_path, 'static', 'uploads')
    filenames = [
        'gallery1.jpg', 'gallery6 .jpg', 'hero.jpg', 
        'slide1.jpg', 'slide2.jpg', 'slide3.jpg'
    ]
    for i, filename in enumerate(filenames, start=1):
        filepath = os.path.join(upload_folder, filename)
        if os.path.exists(filepath):
            db.session.add(GalleryImage(filename=filename, order=i))
        else:
            print(f"⚠️ File non trovato: {filename}")

    # ➤ Collaboratori
    collaborators = [
        Collaborator(name="Mario Rossi", role="Fotografo", bio="Esperto in matrimoni all’aperto."),
        Collaborator(name="Laura Bianchi", role="Videomaker", bio="Ama raccontare storie d'amore in video.")
    ]
    db.session.add_all(collaborators)

    # ➤ Testi dinamici
    texts = [
        EditableText(name="home_title", text_it="Benvenuti nel nostro sito di matrimoni", text_en="Welcome to our wedding site", text_ar="مرحبًا بكم في موقع الزفاف"),
        EditableText(name="home_subtitle", text_it="Organizziamo il vostro giorno speciale", text_en="We plan your special day", text_ar="نخطط ليومكم الخاص")
    ]
    db.session.add_all(texts)

    db.session.commit()
    print("✅ Database popolato con dati iniziali.")

s = Service(title_it="Catering", description_it="Cibo gourmet per ogni gusto", category="Catering", image_filename="catering.jpg")
db.session.add(s)
db.session.commit()
