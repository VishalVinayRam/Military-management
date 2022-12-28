from django.db import models

# Create your models here.
class Family(models.Model):
    name = models.CharField(max_length=50)
    relationship = models.CharField(max_length=50)
    number = models.IntegerField()