from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=200)
    date_pub = models.DateTimeField("date published")
    show = models.IntegerField(default=0)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=1)


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    comment_text = models.CharField(max_length=200)


class Voted(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
