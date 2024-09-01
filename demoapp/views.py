from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home_view(request):
    return HttpResponse("Hello, World!, you are in the demo app. Kudos! fuck")

def bye_view(request):
    return HttpResponse("bye ra halwa bye bye ra")

def view_page(request):
    return render(request, 'demoapp/index.html')