import os

print("🛠️ BUILD — Avvio processo di setup locale...")

# Installa le dipendenze
os.system("pip install -r requirements.txt")

# Crea le cartelle se mancano
for folder in ["instance", "media", "static/pdf"]:
    if not os.path.exists(folder):
        os.makedirs(folder)
        print(f"✅ Cartella creata: {folder}")

# Compila le traduzioni
if os.system("pybabel compile -d translations") == 0:
    print("✅ Traduzioni compilate")
else:
    print("❌ Errore nella compilazione delle traduzioni")

# Inizializza DB se non esiste
if not os.path.exists("instance/booking.db"):
    os.system("python init_db.py")
    print("✅ Database creato")
else:
    print("✅ DB già esistente")

print("✅ BUILD COMPLETATO.")
