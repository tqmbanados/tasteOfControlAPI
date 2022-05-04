from django.db import models


class Instrument(models.Model):
    instrument = models.CharField(max_length=16)
    score_data = models.TextField(default="{}")
    measure = models.IntegerField()
    duration = models.IntegerField(default=6)

    def __str__(self):
        return str(self.instrument)


class Actor(models.Model):
    action = models.CharField(max_length=16, default="None")
    stage = models.CharField(max_length=16, default="0-0")
    number = models.IntegerField(default=0)

    def __str__(self):
        return "Actor"


class FullScore(models.Model):
    score_data = models.TextField(default="{}")

    def __str__(self):
        return "Full Score"


