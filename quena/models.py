from django.db import models
from django.conf import settings
from django.urls.base import reverse

class Question(models.Model):
    title = models.CharField(max_length=140)
    question = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("quena:question_detail", kwargs={"pk": self.id})
    
    def can_accept_answers(self, user):
        return user == self.user
