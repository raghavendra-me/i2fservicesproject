from django import forms
from .models import Contact, Service

class ContactForm(forms.ModelForm):
    services_needed = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )

    class Meta:
        model = Contact
        fields = ['name', 'phone_number', 'email', 'services_needed', 'city_from', 'how_did_you_hear_about_us']
        widgets = {
            'how_did_you_hear_about_us': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({'class': 'form-control'})
        self.fields['phone_number'].widget.attrs.update({'class': 'form-control', 'placeholder': '+1234567890'})
        self.fields['email'].widget.attrs.update({'class': 'form-control'})
        self.fields['city_from'].widget.attrs.update({'class': 'form-control'})
        self.fields['how_did_you_hear_about_us'].widget.attrs.update({'class': 'form-control'})

    def clean_phone_number(self):
        phone_number = self.cleaned_data.get('phone_number')
        if not phone_number:
            raise forms.ValidationError('Phone number is required.')
        return phone_number

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('Email is required.')
        return email

    def clean_services_needed(self):
        services_needed = self.cleaned_data.get('services_needed')
        if not services_needed:
            raise forms.ValidationError('At least one service must be selected.')
        return services_needed