from flask_mail import Message
from flask import current_app
from flask_babel import _
from . import mail

def send_email(subject, recipients, body, html=None):
    msg = Message(subject=subject, recipients=recipients)
    msg.body = body
    if html:
        msg.html = html
    mail.send(msg)

def send_contact_emails(contact):
    admin_email = current_app.config.get('ADMIN_EMAIL') or 'admin@example.com'
    
    # Email utente
    send_email(
        subject=_("Grazie per averci contattato!"),
        body=_("Ti risponderemo al più presto."),
        recipients=[contact.email],   
    )

    # Email admin
    send_email(
        subject="📥 Nuovo messaggio di contatto",
        recipients=[admin_email],
        body=f"""
Nome: {contact.name}
Email: {contact.email}
Telefono: {contact.phone}
Motivo: {contact.reason}
Messaggio:
{contact.message}
"""
    )

def send_booking_emails(booking):
    admin_email = current_app.config.get('ADMIN_EMAIL') or 'admin@example.com'

    # Email utente
    send_email(
        subject=_("Grazie per averci contattato!"),
        body=_("Ti risponderemo al più presto."),
        recipients=[booking.customer_email],
    )

    # Email admin
    send_email(
        subject="📥 Nuova prenotazione ricevuta",
        recipients=[admin_email],
        body=f"""
Nuova prenotazione da {booking.customer_name} ({booking.customer_email})
Telefono: {booking.customer_phone}
Location: {booking.location}
Budget: {booking.budget}
Messaggio:
{booking.message}
"""
    )
