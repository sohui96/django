from django.db import models

class Data(models.Model):
    text = models.CharField(max_length=100)
    cre_date = models.DateTimeField()
