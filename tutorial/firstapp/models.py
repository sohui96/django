from django.db import models

class Curriculum(models.Model):
    name = models.CharField(max_length=255)

    # def __init__(self):
    def __str__(self):
        return self.name
