from django.urls import path
from .views import (
    professor_dashboard,
    course_create,
    course_edit,
    course_delete,
)

urlpatterns = [
    path("dashboard/", professor_dashboard, name="professor_dashboard"),
    path("courses/new/", course_create, name="course_create"),
    path("courses/<int:pk>/edit/", course_edit, name="course_edit"),
    path("courses/<int:pk>/delete/", course_delete, name="course_delete"),
]