import os

languages = ['it', 'en', 'ar']

for lang in languages:
    path = f"translations/{lang}/LC_MESSAGES"
    os.makedirs(path, exist_ok=True)
    print(f"✅ Cartella creata: {path}")

print("✅ Struttura cartelle traduzioni pronta.")
