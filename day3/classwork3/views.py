from django.shortcuts import render

# Create your views here.
def show(request):
    employees = [{'name': 'Rahul','job_title': 'Python Developer','salary': 30000,'is_full_time': True},
        {'name': 'Arun','job_title': 'Web Designer','salary': 25000,'is_full_time': False},
        {'name': 'Anjali','job_title': 'Frontend Developer','salary': 35000,'is_full_time': True}]

    return render(request, 'employees.html',{'employees':employees})