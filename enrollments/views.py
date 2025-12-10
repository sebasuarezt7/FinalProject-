from django.shortcuts import redirect, get_object_or_404
from courses.models import Course
from enrollments.models import Enrollment

def enroll(request, course_id):
    course = get_object_or_404(Course, id=course_id)

    already_enrolled = Enrollment.objects.filter(
        student=request.user, 
        course=course
    ).exists()

    if not already_enrolled:
        Enrollment.objects.create(student=request.user, course=course)

    return redirect("student_dashboard")


def drop_course(request, enrollment_id):
    enrollment = get_object_or_404(
        Enrollment, 
        id=enrollment_id, 
        student=request.user
    )
    enrollment.delete()
    return redirect("student_dashboard")