
from django.shortcuts import render

def home(request):
    return render(request, 'homework9/home.html')
