import os
import filetype
from werkzeug.utils import secure_filename
from flask import current_app as myapp

def allowed_file(filename, filepath=None):
    is_extension_allowed = '.' in filename and \
        filename.rsplit('.', 1)[1].lower() in myapp.config['ALLOWED_EXTENSIONS']
    if not filepath:
        return is_extension_allowed
    kind = filetype.guess(filepath)
    if kind is None:
        return False
    return is_extension_allowed and kind.mime in ['image/jpeg', 'image/png', 'image/gif']

def validate_image_file(file):
    filename = secure_filename(file.filename)
    filepath = os.path.join(myapp.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)
    if not allowed_file(filename, filepath):
        os.remove(filepath)
        return None
    return filename

def validate_and_save_image(file):
    return validate_image_file(file)
