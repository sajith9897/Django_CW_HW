

# Create your views here.
from django.shortcuts import render

def register(request):
    if request.method == 'POST':
        name = request.POST.get('fullname')

        return render(request, 'success.html', {'name': name})

    return render(request, 'register.html')