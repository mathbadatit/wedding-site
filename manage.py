from myapp import create_app, db
from flask_migrate import Migrate
from myapp.commands import register_commands

app = create_app()
migrate = Migrate(app, db)
register_commands(app)

if __name__ == '__main__':
    app.run(debug=True)