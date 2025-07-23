@echo off
call .venv\Scripts\activate

echo === Esegui Migrate DB ===
flask db upgrade

echo === Esegui Seed Dati Demo ===
flask seed-demo

echo === Crea Admin principale ===
flask create-admin --username admin --email admin@example.com --password admin123

echo === Crea Admin multipli da file ===
flask create-admins admins.json

echo === Aggiorna Traduzioni ===
pybabel extract -F babel.cfg -o translations/messages.pot .
pybabel update -i translations/messages.pot -d translations
pybabel compile -d translations

echo === Avvio Server Flask ===
flask run

pause
