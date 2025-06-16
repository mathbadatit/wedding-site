LANGUAGES = [
    ('en', 'English'),
    ('it', 'Italiano'),
    ('ar', 'Arabic'),
]

LANGUAGE_CODE = 'en'
USE_I18N = True
USE_L10N = True
USE_TZ = True

from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent
LOCALE_PATHS = [BASE_DIR / 'locale']

MIDDLEWARE += ['django.middleware.locale.LocaleMiddleware']
