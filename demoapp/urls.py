from django.urls import path
from .views import *
urlpatterns = [
    path('', home_view, name='home'),
    path('about', bye_view, name='about' ),
    path('viewpage', view_page, name='view')
]