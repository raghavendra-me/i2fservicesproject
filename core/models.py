from django.db import models
from django.core.validators import EmailValidator, RegexValidator
import uuid

class Service(models.Model):
    SERVICES_CHOICES = [
        ('visa_validation', 'Visa Validation'),
        ('social_security', 'Social Security'),
        ('bank_account', 'Bank Account'),
        ('transportation', 'Transportation'),
        ('caf_housing_allowance', 'CAF Housing Allowance'),
    ]
    name = models.CharField(max_length=100, choices=SERVICES_CHOICES, unique=True)

    def __str__(self):
        return dict(self.SERVICES_CHOICES).get(self.name, self.name)

class Contact(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=100)
    phone_number = models.CharField(
        max_length=15,
        validators=[RegexValidator(r'^\+?1?\d{9,15}$', 'Enter a valid phone number')]
    )
    email = models.EmailField(validators=[EmailValidator()])
    services_needed = models.ManyToManyField(Service, related_name='contacts', blank=True)
    city_from = models.CharField(max_length=100)
    how_did_you_hear_about_us = models.TextField()

    def __str__(self):
        return self.name
