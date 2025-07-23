. .\.venv\Scripts\Activate.ps1

flask migrate-db
flask seed-demo
flask create-admins admins.json
flask create-admin --username admin --email admin@example.com --password admin123
pybabel extract -F babel.cfg -o translations/messages.pot .
pybabel update -i translations/messages.pot -d translations
pybabel compile -d translations
flask run
