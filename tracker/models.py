from django.db import models

class QuestionTopic(models.Model):
    name = models.CharField(max_length=255)

class Question(models.Model):
    text = models.TextField()
    topics = models.ManyToManyField(QuestionTopic)

class Author(models.Model):
    name = models.CharField(max_length=255)
    url = models.URLField(max_length=1024*5)

class Answer(models.Model):
    votes = models.IntegerField()
    text = models.TextField()
    author = models.ForeignKey(Author)

