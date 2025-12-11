from django.urls import path
from .views import (
    register_student,
    student_login,
    student_dashboard,
    logout_view,
    student_enrollments,
)

urlpatterns = [
    path("register/", register_student, name="register_student"),
    path("login/", student_login, name="student_login"),
    path("dashboard/", student_dashboard, name="student_dashboard"),
    path("logout/", logout_view, name="logout"),
    path("enrollments/", student_enrollments, name="student_enrollments"),
]