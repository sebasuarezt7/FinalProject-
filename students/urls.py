from django.urls import path
from .views import register_student, student_login, student_dashboard

urlpatterns = [
    path("", student_login, name="student_login_default"),  # << Esta línea hace que /students/ vaya al login
    path("register/", register_student, name="register_student"),
    path("login/", student_login, name="student_login"),
    path("dashboard/", student_dashboard, name="student_dashboard"),
]