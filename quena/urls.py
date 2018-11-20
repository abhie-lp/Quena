from . import views
from django.urls import path

app_name = "quena"
urlpatterns = [
    path("", views.QuestionCreateView.as_view(), name="ask"),
    path("question/<int:pk>/", views.QuestionDetailView.as_view(), name="question_detail"),
    path("question/<int:pk>/answer/", views.AnswerCreateView.as_view(), name="answer_question"),
    path("answer/<int:pk>/accept/", views.UpdateAnswerAcceptanceView.as_view(), name="update_answer_acceptance"),
]