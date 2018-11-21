from .forms import UserForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy


class UserRegisterView(CreateView):
    form_class = UserForm
    template_name = "user/register.html"
    success_url = reverse_lazy("user:login")