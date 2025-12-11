from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    capacity = forms.IntegerField(min_value=1, label="Capacity")

    class Meta:
        model = Course
        fields = ["code", "title", "capacity"]