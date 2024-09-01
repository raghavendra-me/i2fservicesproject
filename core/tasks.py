from celery import shared_task
from django.core.mail import send_mail

@shared_task
def send_contact_emails(contact_id):
    contact = Contact.objects.get(id=contact_id)

    subject_admin = f'New Contact Form Submission: {contact.uuid}'
    message_admin = (
        f'A new contact form has been submitted.\n\n'
        f'UUID: {contact.uuid}\n'
        f'Name: {contact.name}\n'
        f'Email: {contact.email}\n'
        f'Phone: {contact.phone_number}\n'
        f'Services Needed: {", ".join([service.name for service in contact.services_needed.all()])}\n'
        f'City From: {contact.city_from}\n'
        f'How Did You Hear About Us: {contact.how_did_you_hear_about_us}\n'
    )
    send_mail(
        subject_admin,
        message_admin,
        settings.DEFAULT_FROM_EMAIL,
        [settings.ADMIN_EMAIL],
        fail_silently=False,
    )

    subject_user = 'Thank You for Contacting Us'
    message_user = (
        f'Dear {contact.name},\n\n'
        f'Thank you for reaching out to us! We have received your details and our team will contact you shortly.\n\n'
        f'Best regards,\n'
        f'The i2fservices Team'
    )
    send_mail(
        subject_user,
        message_user,
        settings.DEFAULT_FROM_EMAIL,
        [contact.email],
        fail_silently=False,
    )