from django.urls import path
from .views import course_list, create_course

urlpatterns = [
    path("", course_list, name="course_list"),
    path("add/", create_course, name="create_course"),
]