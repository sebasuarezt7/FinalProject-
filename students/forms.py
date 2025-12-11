from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

ROLE_CHOICES = [
    ("student", "Student"),
    ("professor", "Professor"),
]

class StudentRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    role = forms.ChoiceField(choices=ROLE_CHOICES, required=True)
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2", "role"]

    def clean_password1(self):
        password = self.cleaned_data.get("password1")
        if len(password) < 6:
            raise forms.ValidationError("Password must be at least 6 characters.")
        return password