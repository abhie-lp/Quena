from . import views
from django.urls import path

app_name = "quena"
urlpatterns = [
    path("", views.QuestionCreateView.as_view(), name="ask"),
]