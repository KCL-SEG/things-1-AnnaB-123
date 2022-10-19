from django.db import models
from django.db.models.Model import Model


# Create your models here.
class Thing(models.Model):
    name = models.charField(max_length=30, unique=True, blank=False)
    description = models.charField(max_length=120, unique=False, blank=True)
    quantity = models.IntegerField(unique=False, blank=False, max_length=100, min_length=0)
