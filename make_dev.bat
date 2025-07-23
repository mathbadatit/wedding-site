@echo off
echo === Attivo ambiente virtuale ===
call .venv\Scripts\activate

echo === Eseguo migrazioni e upgrade ===
flask db migrate -m "Auto migration"
flask db upgrade

echo === Creo l'admin ===
python init_admin.py

echo === Inserisco dati demo ===
flask seed-demo

echo === Aggiorno traduzioni ===
pybabel extract -F babel.cfg -o translations/messages.pot .
pybabel update -i translations/messages.pot -d translations
pybabel compile -d translations

echo === Avvio server Flask in locale ===
flask run

pause
