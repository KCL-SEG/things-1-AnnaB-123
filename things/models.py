from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Model

# Create your models here.
class Thing(Model):
    name = models.CharField(max_length=30, unique=True, blank=False)
    description = models.CharField(max_length=120, unique=False, blank=True)
    quantity = models.IntegerField(unique=False, blank=False,validators=[MinValueValidator(0), MaxValueValidator(100)])
