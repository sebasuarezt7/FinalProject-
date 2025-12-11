from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from courses.models import Course
from enrollments.models import Enrollment


@login_required
def enroll(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    student = request.user.student

    already_enrolled = Enrollment.objects.filter(
        student=student,
        course=course
    ).exists()

    if already_enrolled:
        messages.warning(request, "You are already enrolled in this course.")
    else:
        Enrollment.objects.create(student=student, course=course)
        messages.success(request, "Enrollment completed successfully!")

    return redirect("student_dashboard")


@login_required
def drop_course(request, enrollment_id):
    student = request.user.student

    enrollment = get_object_or_404(
        Enrollment,
        id=enrollment_id,
        student=student
    )
    enrollment.delete()
    messages.success(request, "Enrollment removed.")
    return redirect("student_enrollments")