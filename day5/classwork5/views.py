

# Create your views here.
from django.shortcuts import render
from .forms import LoginForm

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            return render(request,'form-data.html',{
                'message': 'Thankyou...',
                'email': form['email'].value,
                'password': form['password'].value
             })
    else:
        form = LoginForm()
    return render(request,'user_login.html',{'form':form})