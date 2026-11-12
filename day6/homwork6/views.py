from django.shortcuts import render
from .models import Contact

def contact(request):

    if request.method == 'POST':

        name = request.POST.get('full_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        Contact.objects.create(
            full_name=name,
            email=email,
            phone=phone
        )

        return render(request, 'homework6/thankyou.html', {'name': name})

    return render(request, 'homework6/contact.html')