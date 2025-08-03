from flask import Blueprint, render_template
from myapp.models import Service

services_bp = Blueprint('services', __name__, url_prefix='/services')

@services_bp.route('/')
def list():
    services = Service.query.all()
    categories = sorted(set([s.category for s in services if s.category]))
    return render_template('services.html', services=services, categories=categories)

@services_bp.route('/modal/<int:service_id>')
def modal(service_id):
    service = Service.query.get_or_404(service_id)
    return render_template('partials/service_modal.html', service=service)

@services_bp.route('/<int:service_id>')  # <-- Qui la route detail
def detail(service_id):
    service = Service.query.get_or_404(service_id)
    return render_template('service_detail.html', service=service)
