@echo off
echo 🔄 Resetting database...

REM [OPZIONALE] Cancella il vecchio DB
IF EXIST "instance\app.db" (
    del "instance\app.db"
    echo ✅ Vecchio database rimosso.
)

REM Migra il database
echo 🗂️ Migrating DB...
flask db upgrade

REM Seed: categorie e servizi
echo 🌱 Seeding dati demo...
python seed.py

REM Avvia server con auto-reload
echo 🚀 Avvio Flask...
start "" http://127.0.0.1:5000/
flask run --reload
