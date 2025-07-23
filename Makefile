.PHONY: activate migrate seed create_admins create_admin babel run all

activate:
	. .venv/Scripts/activate

migrate:
	flask migrate-db

seed:
	flask seed-demo

create_admins:
	flask create-admins admins.json

create_admin:
	flask create-admin --username=admin --email=admin@example.com --password=admin123

babel:
	pybabel extract -F babel.cfg -o translations/messages.pot .
	pybabel update -i translations/messages.pot -d translations
	pybabel compile -d translations

run:
	flask run

all: migrate seed create_admins create_admin babel run
