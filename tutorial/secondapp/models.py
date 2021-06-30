from django.db import models

class Hospital(models.Model):
    id = models.CharField(max_length=50, primary_key=True)
    sido = models.CharField(max_length=50)
    name = models.CharField(max_length=50)
    medical = models.IntegerField(max_length=50)
    room = models.CharField(max_length=50)
    tel = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

def __str__(self):
    return self.name
