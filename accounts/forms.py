from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User


class RegisterForm(UserCreationForm):

    class Meta:
        model = User

        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "phone",
            "city",
            "role",
            "password1",
            "password2",
        )

        widgets = {
            "role": forms.Select(attrs={"class": "form-select"}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        placeholders = {
            "username": "Enter Username",
            "first_name": "First Name",
            "last_name": "Last Name",
            "email": "Email Address",
            "phone": "Phone Number",
            "city": "City",
            "password1": "Password",
            "password2": "Confirm Password",
        }

        for name, field in self.fields.items():

            if name == "role":
                field.widget.attrs.update({
                    "class": "form-select"
                })
            else:
                field.widget.attrs.update({
                    "class": "form-control",
                    "placeholder": placeholders.get(name, "")
                })


class LoginForm(AuthenticationForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Username"
        })

        self.fields["password"].widget.attrs.update({
            "class": "form-control",
            "placeholder": "Password"
        })