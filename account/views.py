from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render


def register(request):
    if request.method == "POST":
        user_form = UserCreationForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            return redirect("login")
    else:
        user_form = UserCreationForm()
    return render(request, "register.html", {"user_form": user_form})


def login_admin(request):
    login_form = AuthenticationForm()

    if request.method == "POST":
        login_form = AuthenticationForm(request, request.POST)
        if login_form.is_valid():
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                return login_form
    return render(request, "login.html", {"form": login_form})


def logout_admin(request):
    logout(request)
    return redirect("login")
