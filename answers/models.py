from django.db import models


class Answer(models.Model):
    answer = models.IntegerField(default=0)
    pair = models.CharField(max_length=10, default="")

    def __str__(self):
        return self.pair + " : " + self.answer