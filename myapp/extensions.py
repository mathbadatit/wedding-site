from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_mail import Mail
from flask_babel import Babel
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager
from flask_jwt_extended import JWTManager

db = SQLAlchemy()
migrate = Migrate()
mail = Mail()
babel = Babel()
csrf = CSRFProtect()
login_manager = LoginManager()
jwt = JWTManager()

login_manager.login_view = 'admin.login'
