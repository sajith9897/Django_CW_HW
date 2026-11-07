from django.shortcuts import render

def home(request):
    return render(request, 'visitor.html')


def result(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        color = request.POST.get('color')

        return render(request, 'data_result.html', {
            'name': name,
            'color': color
        })

    return render(request, 'visitor.html')