from flask import Blueprint

api_bp = Blueprint('api', __name__)

from . import routes  # o file simili per gestire rotte API