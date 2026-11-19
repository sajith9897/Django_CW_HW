from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm


# Display and search students
def student_list(request):
    query = request.GET.get('search', '').strip()

    students = Student.objects.all().order_by('id')

    if query:
        students = students.filter(name__icontains=query)

    return render(request, 'homework10/student_list.html', {
        'students': students,
        'query': query
    })


# Add student
def add_student(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()

    return render(request, 'homework10/student_form.html', {
        'form': form,
        'heading': 'Add Student'
    })


# Edit student
def edit_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)

        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)

    return render(request, 'homework10/student_form.html', {
        'form': form,
        'heading': 'Edit Student'
    })


# Delete student
def delete_student(request, id):
    student = get_object_or_404(Student, id=id)

    if request.method == 'POST':
        student.delete()
        return redirect('student_list')

    return render(request, 'homework10/student_delete.html', {
        'student': student
    })