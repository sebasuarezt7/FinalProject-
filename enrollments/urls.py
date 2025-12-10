from django.urls import path
from .views import enroll, drop_course

urlpatterns = [
    path("enroll/<int:course_id>/", enroll, name="enroll"),
    path("drop/<int:enrollment_id>/", drop_course, name="drop_course"),
]