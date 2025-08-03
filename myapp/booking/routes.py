from flask import render_template, request, redirect, url_for, flash
from myapp.extensions import db
from myapp.models import Booking, Service
from myapp.forms.booking_forms import BookingForm
from . import booking_bp

@booking_bp.route('/book', methods=['GET', 'POST'])
def book():
    form = BookingForm()
    form.service_id.choices = [(s.id, s.title_it) for s in Service.query.all()]
    if form.validate_on_submit():
        booking = Booking(
            name=form.name.data,
            email=form.email.data,
            phone=form.phone.data,
            location=form.location.data,
            budget=form.budget.data,
            message=form.message.data,
            service_id=form.service_id.data
        )
        db.session.add(booking)
        db.session.commit()
        flash('Prenotazione inviata!', 'success')
        return redirect(url_for('main.home'))
    return render_template('booking.html', form=form)
