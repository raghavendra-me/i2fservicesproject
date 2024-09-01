from django.shortcuts import render, redirect
from .forms import ContactForm
from django.core.mail import send_mail
from django.conf import settings


# def home_page(request):
#     return render(request, 'core/index.html')

def home_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect or handle success
    else:
        form = ContactForm()

    return render(request, 'core/index.html', {'form': form})

def contact_page(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save the form data to the database
            contact = form.save()

            # Extract selected services (ManyToManyField)
            selected_services = ', '.join([service.name for service in contact.services_needed.all()])

            # Send email to admin with UUID and form details
            subject_admin = f'New Contact Form Submission: {contact.uuid}'
            message_admin = (
                f'A new contact form has been submitted.\n\n'
                f'UUID: {contact.uuid}\n'
                f'Name: {contact.name}\n'
                f'Email: {contact.email}\n'
                f'Phone: {contact.phone_number}\n'
                f'Services Needed: {selected_services}\n'  # Updated for ManyToManyField
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

            # Send confirmation email to the user
            # subject_user = 'Thank You for Contacting Us'
            # message_user = (
            #     f'Dear {contact.name},\n\n'
            #     f'Thank you for reaching out to us! We have received your details and our team will contact you shortly.\n\n'
            #     f'Best regards,\n'
            #     f'The i2fservices Team'
            # )
            # send_mail(
            #     subject_user,
            #     message_user,
            #     settings.DEFAULT_FROM_EMAIL,
            #     [contact.email],
            #     fail_silently=False,
            # )

            return redirect('success')  # Change to the success page URL you want
    else:
        form = ContactForm()

    return render(request, 'core/contact-us.html', {'form': form})

# from .tasks import send_contact_emails

# def contact_page(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             contact = form.save()

#             # Call the task to send emails
#             send_contact_emails.delay(contact.id)

#             return redirect('success')
#     else:
#         form = ContactForm()

#     return render(request, 'core/contact-us.html', {'form': form})

def success_page(request):
    return render(request, 'core/success.html')

# def contact_page(request):
#     if request.method == 'POST':
#         form = ContactForm(request.POST)
#         form.save()
#         return redirect('home')
    
#     else:
#         form = ContactForm()
    
#     return render(request, 'core/contact-us.html', {'form': form})