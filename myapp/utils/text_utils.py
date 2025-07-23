import uuid
from werkzeug.utils import secure_filename
from myapp.models import EditableText

def generate_slug(title):
    return secure_filename(title.lower().replace(" ", "-"))

def unique_filename(filename):
    ext = filename.rsplit('.', 1)[1] if '.' in filename else ''
    unique_id = uuid.uuid4().hex
    return f"{unique_id}.{ext}"

def get_text(key, default=''):
    record = EditableText.query.filter_by(key=key).first()
    return record.content if record else default
