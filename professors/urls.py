from django.urls import path
from .views import professor_dashboard

urlpatterns = [
    path("", professor_dashboard, name="professor_dashboard"),
]