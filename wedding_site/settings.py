import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# ...

LANGUAGE_CODE = 'it'  # o 'en' se preferisci

# Percorsi media (upload)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Static (es. CSS)
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
