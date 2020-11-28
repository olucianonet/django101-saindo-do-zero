from django.db import models


class Task(models.Model):
    title = models.CharField('título', max_length=25)
    description = models.TextField('descrição', max_length=50)
    done = models.BooleanField(default=False)

