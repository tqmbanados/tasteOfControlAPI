from django.db import models


class Instrument(models.Model):
    instrument = models.CharField(max_length=16)
    score_data = models.TextField()
    measure = models.IntegerField()

    def __str__(self):
        return str(self.instrument) + str(self.measure)
