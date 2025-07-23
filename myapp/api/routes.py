from flask import request, jsonify
from flask_jwt_extended import jwt_required
from myapp.extensions import db
from myapp.models import Service
from . import api_bp

@api_bp.route('/services', methods=['GET'])
def get_services():
    services = Service.query.all()
    return jsonify([{"id": s.id, "title": s.title, "description": s.description} for s in services])

@api_bp.route('/services', methods=['POST'])
@jwt_required()
def create_service():
    data = request.json
    if not data.get('title') or not data.get('description'):
        return jsonify({"error": "Invalid input"}), 400

    service = Service(title=data['title'], description=data['description'])
    db.session.add(service)
    db.session.commit()
    return jsonify({"message": "Service created", "id": service.id}), 201

@api_bp.route('/services/<int:id>', methods=['PUT'])
@jwt_required()
def update_service(id):
    service = Service.query.get_or_404(id)
    data = request.json
    service.title = data.get('title', service.title)
    service.description = data.get('description', service.description)
    db.session.commit()
    return jsonify({"message": "Service updated"})

@api_bp.route('/services/<int:id>', methods=['DELETE'])
@jwt_required()
def delete_service(id):
    service = Service.query.get_or_404(id)
    db.session.delete(service)
    db.session.commit()
    return jsonify({"message": "Service deleted"})
