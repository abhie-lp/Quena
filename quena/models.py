from django.db import models
from django.conf import settings
from django.urls.base import reverse
from .service import elasticsearch

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
    
    def as_elasticsearch_dict(self):
        return {
            "_id": self.id,
            "_type": "doc",
            "text": "{}\n{}".format(self.title, self.question),
            "question_body": self.question,
            "title": self.title,
            "id": self.id,
            "created": self.created,
        }
    
    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save(force_insert=force_insert,
                    force_update=force_update,
                    using=using,
                    update_fields=update_fields)
        elasticsearch.upsert(self)


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    accepted = models.BooleanField(default=False)

    class Meta:
        ordering = "-created",
    
    def __str__(self):
        return self.question.title
