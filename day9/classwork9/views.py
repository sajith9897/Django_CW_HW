
from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import Http404

students = {
    "Rahul": {"maths": 85, "science": 90, "english": 80},
    "Arjun": {"maths": 75, "science": 82, "english": 78},
    "Anu": {"maths": 95, "science": 92, "english": 96},
    "Meera": {"maths": 88, "science": 85, "english": 90},
    "Vishnu": {"maths": 65, "science": 70, "english": 72},
}


def home(request):
    return render(request, "classwork9/home.html", {
        "students": students
    })


def login_page(request, name):
    if name not in students:
        raise Http404("Student not found")

    error = None

    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == "admin" and password == "1234":
            request.session["result_access"] = True
            return redirect("classwork9:result", name=name)
        else:
            error = "Invalid username or password"

    return render(request, "classwork9/login.html", {
        "name": name,
        "error": error
    })


def result(request, name):
    if name not in students:
        raise Http404("Student not found")

    if not request.session.get("result_access"):
        return redirect("classwork9:login", name=name)

    student = students[name]
    total = sum(student.values())
    percentage = total / 3

    if any(mark < 35 for mark in student.values()):
        grade = "F"
        status = "Fail"
    elif percentage >= 90:
        grade = "A+"
        status = "Pass"
    elif percentage >= 80:
        grade = "A"
        status = "Pass"
    elif percentage >= 70:
        grade = "B"
        status = "Pass"
    elif percentage >= 60:
        grade = "C"
        status = "Pass"
    else:
        grade = "D"
        status = "Pass"

    return render(request, "classwork9/result.html", {
        "name": name,
        "student": student,
        "total": total,
        "percentage": round(percentage, 2),
        "grade": grade,
        "status": status
    })
