from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from social.models import Posts
from django.forms import CharField, Form, PasswordInput


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["first_name",
                  "last_name",
                  "username",
                  "email",
                  "password1"]
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control", "rows": 3}),
            "last_name": forms.TextInput(attrs={"class": "form-control", "rows": 3}),
            "username": forms.TextInput(attrs={"class": "form-control", "rows": 3}),
            "email": forms.TextInput(attrs={"class": "form-control", "rows": 3}),
            "password1": forms.TextInput(attrs={"class": "form-control", "rows": 3}),
            "password2": forms.TextInput(attrs={"class": "form-control", "rows": 3}),
        }
        help_texts = {
            'first_name': None,
            'last_name"': None,
            'username': None,
            'email': None,
            'password1': None,
            # 'password1':None,
        }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['password1'].help_text = 'Your text'
            self.fields['password2'].help_text = 'Your text'


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TimeInput(attrs={"class": "form-control"}))
    password = forms.CharField(
        widget=PasswordInput(attrs={"class": "form-control"}))


class PostsForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = [
            "title",
            "images"
        ]

        widgets = {
            "title": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "images": forms.FileInput(attrs={"class": "form-select"})
        }
