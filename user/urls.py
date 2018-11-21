from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

app_name = "user"
urlpatterns = [
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
]