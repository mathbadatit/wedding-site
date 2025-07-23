@echo off
REM Attiva l'ambiente virtuale
call .venv\Scripts\activate.bat

REM (Opzionale) Installa dipendenze
pip install -r requirements.txt

REM Avvia Flask in debug mode
set FLASK_APP=manage.py
set FLASK_ENV=development
flask run

pause
