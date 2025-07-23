from flask import render_template, jsonify, request
from myapp.admin import bp
from myapp.extensions import db
from myapp.models import Service  # esempio modello SQLAlchemy

@bp.route('/services')
def admin_services():
    return render_template('admin_services.html')

@bp.route('/api/services', methods=['GET'])
def get_services():
    services = Service.query.all()
    data = [{"id": s.id, "title": s.title_it, "description": s.description_it, "image_url": s.image_url} for s in services]
    return jsonify(data)

@bp.route('/api/services', methods=['POST'])
def add_or_update_service():
    data = request.json
    if data.get('id'):
        service = Service.query.get(data['id'])
        if service:
            service.title_it = data['title']
            service.description_it = data['description']
            service.image_url = data['image_url']
    else:
        service = Service(title_it=data['title'], description_it=data['description'], image_url=data['image_url'])
        db.session.add(service)
    db.session.commit()
    return jsonify({"success": True})

@bp.route('/api/services/<int:id>', methods=['DELETE'])
def delete_service(id):
    service = Service.query.get(id)
    if service:
        db.session.delete(service)
        db.session.commit()
    return jsonify({"success": True})
