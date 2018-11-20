from django.contrib import admin
from .models import Question, Answer

class AnswerInline(admin.TabularInline):
    model = Answer


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = "title", "user", "created",
    list_filter = "created", "updated",
    search_fields = "title",
    inlines = AnswerInline,


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = "question", "user", "created", "accepted",
    list_filter = "created", "updated",
    list_editable = "accepted",
    search_fields = "question", "answer",