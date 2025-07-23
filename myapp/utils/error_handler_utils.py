from flask import render_template
from myapp.utils.logging_utils import log_error

def register_error_handlers(app):
    @app.errorhandler(404)
    def page_not_found(e):
        log_error(f'404 Not Found: {e}')
        return render_template('errors/404.html'), 404

    @app.errorhandler(500)
    def internal_error(e):
        log_error(f'500 Internal Server Error: {e}')
        return render_template('errors/500.html'), 500
