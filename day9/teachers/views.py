
from django.shortcuts import render

def teacher_list(request, message):

    teachers = [
        {'id': 201, 'name': 'Anil Kumar', 'subject': 'Mathematics'},
        {'id': 202, 'name': 'Priya Nair', 'subject': 'Computer Science'},
        {'id': 203, 'name': 'Suresh', 'subject': 'Physics'},
        {'id': 204, 'name': 'Deepa', 'subject': 'English'},
        {'id': 205, 'name': 'Ramesh', 'subject': 'Chemistry'},
    ]

    return render(request, 'teachers/teacher_list.html', {
        'teachers': teachers,
        'message': message
    })
