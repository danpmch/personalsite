from django.db import models
from markdownx.models import MarkdownxField

class Topic(models.Model):
    name = models.CharField(max_length=256)
    description = models.CharField(max_length=4096)

    def __str__(self):
        return self.name


class Article(models.Model):
    topic = models.ForeignKey(
        to=Topic,
        null=True,
        on_delete=models.SET_NULL,
    )
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=4096)
    published = models.DateTimeField("date published")

    body = MarkdownxField(default='')

    def __str__(self):
        return self.title
