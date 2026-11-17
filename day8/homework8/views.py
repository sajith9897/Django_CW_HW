from django.shortcuts import render

def home(request):
    return render(request, 'homework8/home.html')

def about(request):
    return render(request, 'homework8/about.html')