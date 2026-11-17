
from django.shortcuts import render

def student_list(request, message):

    students = [
        {'id': 101, 'name': 'Rahul', 'course': 'BCA', 'year': 1},
        {'id': 102, 'name': 'Arjun', 'course': 'BSc CS', 'year': 2},
        {'id': 103, 'name': 'Anu', 'course': 'BCom', 'year': 3},
        {'id': 104, 'name': 'Meera', 'course': 'BBA', 'year': 1},
        {'id': 105, 'name': 'Vishnu', 'course': 'BCA', 'year': 2},
    ]

    return render(request, 'students/student_list.html', {
        'students': students,
        'message': message
    })
