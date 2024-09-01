from django.urls import path
from .views import *
urlpatterns = [
    path('',home_page, name='home'),
    path('contact-us',contact_page,name='contact'),
    path('success',success_page,name='success'),
]