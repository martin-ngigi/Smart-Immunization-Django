from django.db import models

# Create your models here.

from django.utils import timezone
now = timezone.now()

class Immunizations(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email =  models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    age = models.CharField(max_length=3)
    nationId = models.CharField(max_length=8)
    immunizationName = models.CharField(max_length=30)
    immunizationDosageLevel=models.CharField(max_length=30)
    immunizationDate =models.CharField(max_length=20)
    nextImmunizationDate = models.CharField(max_length=30)
    county = models.CharField(max_length=30)

