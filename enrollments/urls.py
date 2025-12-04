from django.urls import path
from . import views

urlpatterns = [
    path('', views.enrollment_list, name='enrollment_list'),
]