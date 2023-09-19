# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

    def clean_username(self):
        username = self.cleaned_data.get("username")
        try:
            user = User.objects.get(username=username)
            raise forms.ValidationError(
                "This username is already taken. Please choose a different one."
            )
        except User.DoesNotExist:
            return username
