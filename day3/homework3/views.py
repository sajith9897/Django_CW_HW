from django.shortcuts import render

# Create your views here.
def list(request):

    students = [
        {
            'name': 'Rahul',
            'grade': 'A',
            'passed': True
        },
        {
            'name': 'Anjali',
            'grade': 'B',
            'passed': True
        },
        {
            'name': 'Arun',
            'grade': 'D',
            'passed': False
        },
        {
            'name': 'Amal',
            'grade': 'C',
            'passed': True
        }
    ]

    return render(request, 'students.html', {'students': students})