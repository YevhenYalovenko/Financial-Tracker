from django.contrib.auth import views as auth_views
from django.urls import path

from . import views

app_name = "tracker"

urlpatterns = [
    path("register/", views.register, name="register"),
    path("login/", views.login_view, name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
