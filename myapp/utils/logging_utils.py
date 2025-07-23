import logging
import os

# Config log livello base e formato
LOG_LEVEL = os.getenv('APP_LOG_LEVEL', 'INFO').upper()

logging.basicConfig(
    level=LOG_LEVEL,
    format='[%(asctime)s] %(levelname)s in %(module)s: %(message)s'
)

logger = logging.getLogger('myapp')

def log_info(message):
    logger.info(message)

def log_warning(message):
    logger.warning(message)

def log_error(message):
    logger.error(message)

def log_exception(message):
    logger.exception(message)  # Usalo nei blocchi try/except
