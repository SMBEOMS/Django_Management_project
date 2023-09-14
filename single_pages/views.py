from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

def landing(request):
    return render(
        request,
        'single_pages/landing.html'
    )
def home(request):
    return render(
        request,
        'single_pages/home.html'
    )