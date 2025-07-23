from flask import jsonify, request
from flask_login import login_required
from . import bp
from myapp.models import Service
from myapp.extensions import db

@bp.route('/api/services', methods=['GET'])
@login_required
def get_services():
    services = Service.query.all()
    data = [{"id": s.id, "title": s.title_it, "description": s.description_it, "image_url": s.image_url} for s in services]
    return jsonify(data)

@bp.route('/api/services', methods=['POST'])
@login_required
def add_or_update_service():
    data = request.json
    if not data:
        return jsonify({"error": "No input data provided"}), 400

    if data.get('id'):
        service = Service.query.get(data['id'])
        if not service:
            return jsonify({"error": "Service not found"}), 404
        service.title_it = data.get('title', service.title_it)
        service.description_it = data.get('description', service.description_it)
        service.image_url = data.get('image_url', service.image_url)
    else:
        service = Service(
            title_it=data.get('title'),
            description_it=data.get('description'),
            image_url=data.get('image_url')
        )
        db.session.add(service)
    db.session.commit()
    return jsonify({"success": True})

@bp.route('/api/services/<int:id>', methods=['DELETE'])
@login_required
def delete_service(id):
    service = Service.query.get(id)
    if not service:
        return jsonify({"error": "Service not found"}), 404
    db.session.delete(service)
    db.session.commit()
    return jsonify({"success": True})
