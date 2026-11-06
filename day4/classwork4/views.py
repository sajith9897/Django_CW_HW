# Create your views here.
from django.shortcuts import render
def login(request):
    if request.GET:
        username = request.GET.get('username')
        return render(request,'result.html',{
            'resultData':request.GET,
            'username': username
        })
    return render(request,'login_form.html' )