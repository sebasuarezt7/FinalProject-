from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class StudentRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        if len(password) < 6:
            raise forms.ValidationError("Password must be at least 6 characters.")
        return password