from django.urls import path

from . import views

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_admin, name="login"),
    path("logout/", views.logout_admin, name="logout"),
]
