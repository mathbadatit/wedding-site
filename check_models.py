from myapp import create_app
from myapp.models import GalleryImage, User

app = create_app()

with app.app_context():
    # Controllo GalleryImage
    assert hasattr(GalleryImage, 'order'), "❌ GalleryImage: manca il campo 'order'"
    assert hasattr(GalleryImage, 'filename'), "❌ GalleryImage: manca 'filename'"

    # Controllo User
    assert hasattr(User, 'email'), "❌ User: manca il campo 'email'"
    assert hasattr(User, 'set_password'), "❌ User: manca il metodo set_password()"

    print("✅ Tutti i modelli hanno i campi richiesti.")
