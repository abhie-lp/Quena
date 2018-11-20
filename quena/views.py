from .models import Question
from .forms import QuestionForm
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView
from django.http import HttpResponseBadRequest


class QuestionCreateView(LoginRequiredMixin, CreateView):
    form_class = QuestionForm
    template_name = "quena/ask.html"

    def get_initial(self):
        return {
            "user": self.request.user.id,
        }
    
    def form_valid(self, form):
        action = self.request.POST.get("action")
        if action == "SAVE":
            return super().form_valid(form)
        elif action == "PREVIEW":
            preview = Question(
                question = form.cleaned_data["question"],
                title = form.cleaned_data["title"],
            )
            ctx = self.get_context_data(preview=preview)
            return self.render_to_response(context=ctx)
        return HttpResponseBadRequest