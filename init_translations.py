import os

languages = ['it', 'en', 'ar']

for lang in languages:
    cmd = f'pybabel init -i messages.pot -d translations -l {lang}'
    result = os.system(cmd)
    if result == 0:
        print(f"✅ Inizializzato {lang}")
    else:
        print(f"❌ Errore inizializzazione {lang} (probabile già creato)")
