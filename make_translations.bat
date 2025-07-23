@echo off
echo === Attivo ambiente virtuale ===
call .venv\Scripts\activate

echo === Aggiorno Traduzioni ===
pybabel extract -F babel.cfg -o translations/messages.pot .
pybabel update -i translations/messages.pot -d translations
pybabel compile -d translations

echo === Fatto ===
