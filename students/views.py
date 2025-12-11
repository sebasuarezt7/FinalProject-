from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .forms import StudentRegisterForm
from courses.models import Course
from enrollments.models import Enrollment
from students.models import Student
from professors.models import Professor


def logout_view(request):
    logout(request)
    return redirect("/")   # te manda directo al home


def register_student(request):
    if request.method == "POST":
        form = StudentRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            role = form.cleaned_data.get("role", "student")
            email = form.cleaned_data["email"]

            if role == "student":
                Student.objects.create(
                    user=user,
                    name=user.username,
                    email=email,
                )
                login(request, user)
                return redirect("student_dashboard")

            elif role == "professor":
                Professor.objects.create(
                    user=user,
                    name=user.username,
                    email=email,
                )
                login(request, user)
                return redirect("professor_dashboard")

    else:
        form = StudentRegisterForm()

    return render(request, "students/register.html", {"form": form})


def student_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            # Si es profesor, lo mandamos a su dashboard
            if hasattr(user, "professor"):
                return redirect("professor_dashboard")

            # Si es estudiante, a su dashboard
            return redirect("student_dashboard")

        return render(request, "students/login.html", {"error": "Invalid credentials"})

    return render(request, "students/login.html")


@login_required
def student_dashboard(request):
    if not hasattr(request.user, "student"):
        return redirect("professor_dashboard")

    student = request.user.student

    search_query = request.GET.get("q", "").strip()


    courses = Course.objects.all()

    if search_query:
        courses = courses.filter(
            Q(code__icontains=search_query) |
            Q(title__icontains=search_query)
        )

    # enrollments student
    my_enrollments = Enrollment.objects.filter(student=student)
    enrolled_course_ids = my_enrollments.values_list("course_id", flat=True)

    return render(request, "students/dashboard.html", {
        "courses": courses,
        "my_enrollments": my_enrollments,
        "enrolled_course_ids": enrolled_course_ids,
        "search_query": search_query,  
    })


@login_required
def student_enrollments(request):
    """
    Página separada para ver las inscripciones del estudiante.
    """
    student = request.user.student
    my_enrollments = Enrollment.objects.filter(student=student)

    return render(request, "students/enrollments.html", {
        "my_enrollments": my_enrollments,
    })