from django.db import models
from django.urls.resolvers import LocalePrefixPattern

class Point(models.Model):
    title = models.CharField(max_length=100)
    lat = models.FloatField()
    lng = models.FloatField()