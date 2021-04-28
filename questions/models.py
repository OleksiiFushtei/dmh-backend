from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=200, blank=False)
    pair = models.CharField(max_length=20, blank=False, default='')

    def __str__(self):
        return self.title