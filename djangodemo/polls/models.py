from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)  # this will be used both by db and django validation
    publish_date = models.DateTimeField(
        "date published")  # human-readable label, always first positional argument (optional)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)  # SQL equivalent of ON DELETE CASCADE
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
