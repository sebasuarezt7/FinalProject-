from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .forms import StudentRegisterForm
from courses.models import Course
from enrollments.models import Enrollment
from students.models import Student

def register_student(request):
    if request.method == "POST":
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            Student.objects.create(
                user=user,
                name=user.username,
                email=form.cleaned_data["email"],
            )

            login(request, user)
            return redirect("student_dashboard")
    else:
        form = StudentRegisterForm()

    return render(request, "students/register.html", {"form": form})


def student_login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)
            return redirect("student_dashboard")

        return render(request, "students/login.html", {"error": "Invalid credentials"})

    return render(request, "students/login.html")


@login_required
def student_dashboard(request):
    courses = Course.objects.all()

    my_enrollments = Enrollment.objects.filter(student=request.user.student)

    enrolled_course_ids = my_enrollments.values_list("course_id", flat=True)

    return render(request, "students/dashboard.html", {
        "courses": courses,
        "my_enrollments": my_enrollments,
        "enrolled_course_ids": enrolled_course_ids
    })
