from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import RegisterForm, LoginForm


def register(request):

    if request.method == "POST":

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save()

            login(request, user)

            # Admin Redirect
            if user.is_superuser or user.is_staff:
                return redirect("/admin/")

            # Worker Redirect (dashboard later)
            elif user.role == "worker":
                return redirect("home")

            # Customer Redirect (dashboard later)
            else:
                return redirect("home")

    else:
        form = RegisterForm()

    return render(request, "accounts/register.html", {"form": form})


def login_view(request):

    if request.method == "POST":

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            user = form.get_user()

            login(request, user)

            # Admin Redirect
            if user.is_superuser or user.is_staff:
                return redirect("/admin/")

            # Worker Redirect (dashboard later)
            elif user.role == "worker":
                return redirect("home")

            # Customer Redirect (dashboard later)
            else:
                return redirect("home")

    else:
        form = LoginForm()

    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):

    logout(request)

    return redirect("home")