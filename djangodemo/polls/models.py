import datetime

from django.utils import timezone

from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)  # this will be used both by db and django validation
    publish_date = models.DateTimeField(
        "date published")  # human-readable label, always first positional argument (optional)

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.publish_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # SQL equivalent of ON DELETE CASCADE
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.choice_text} {self.votes}"
