from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q 
from courses.models import Course
from courses.forms import CourseForm


def user_is_professor(user):
    return hasattr(user, "professor")


@login_required
def professor_dashboard(request):
    if not user_is_professor(request.user):
        return redirect("student_dashboard")

    search_query = request.GET.get("q", "").strip()

    courses = Course.objects.all()

    if search_query:
        courses = courses.filter(
            Q(code__icontains=search_query) |
            Q(title__icontains=search_query)
        )

    return render(request, "professors/dashboard.html", {
        "courses": courses,
        "search_query": search_query,
    })

@login_required
def course_create(request):
    if not user_is_professor(request.user):
        return redirect("student_dashboard")

    if request.method == "POST":
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("professor_dashboard")
    else:
        form = CourseForm()

    return render(request, "professors/course_form.html", {
        "form": form,
        "title": "Create Course",
    })


@login_required
def course_edit(request, pk):
    if not user_is_professor(request.user):
        return redirect("student_dashboard")

    course = get_object_or_404(Course, pk=pk)

    if request.method == "POST":
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect("professor_dashboard")
    else:
        form = CourseForm(instance=course)

    return render(request, "professors/course_form.html", {
        "form": form,
        "title": "Edit Course",
    })


@login_required
def course_delete(request, pk):
    if not user_is_professor(request.user):
        return redirect("student_dashboard")

    course = get_object_or_404(Course, pk=pk)

    if request.method == "POST":
        course.delete()
        return redirect("professor_dashboard")

    return render(request, "professors/course_confirm_delete.html", {
        "course": course
    })